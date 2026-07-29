import numpy as np
import pandas as pd


INITIAL_FEATURES = [
    "NAME_CONTRACT_TYPE",
    "CODE_GENDER",
    "FLAG_OWN_CAR",
    "FLAG_OWN_REALTY",
    "CNT_CHILDREN",
    "CNT_FAM_MEMBERS",
    "AMT_INCOME_TOTAL",
    "AMT_CREDIT",
    "AMT_ANNUITY",
    "AMT_GOODS_PRICE",
    "NAME_INCOME_TYPE",
    "NAME_EDUCATION_TYPE",
    "NAME_FAMILY_STATUS",
    "NAME_HOUSING_TYPE",
    "OCCUPATION_TYPE",
    "ORGANIZATION_TYPE",
    "DAYS_BIRTH",
    "DAYS_EMPLOYED",
    "DAYS_REGISTRATION",
    "DAYS_ID_PUBLISH",
    "REGION_POPULATION_RELATIVE",
    "REGION_RATING_CLIENT",
    "REGION_RATING_CLIENT_W_CITY",
    "EXT_SOURCE_1",
    "EXT_SOURCE_2",
    "EXT_SOURCE_3",
    "AMT_REQ_CREDIT_BUREAU_HOUR",
    "AMT_REQ_CREDIT_BUREAU_DAY",
    "AMT_REQ_CREDIT_BUREAU_WEEK",
    "AMT_REQ_CREDIT_BUREAU_MON",
    "AMT_REQ_CREDIT_BUREAU_QRT",
    "AMT_REQ_CREDIT_BUREAU_YEAR",
]


def safe_divide(
    numerator: pd.Series,
    denominator: pd.Series,
) -> pd.Series:
    """
    Safely divide two pandas Series.

    Zero and missing denominators are converted to missing values.
    Infinite results are also replaced with missing values.
    """
    denominator_clean = denominator.replace(0, np.nan)

    result = numerator / denominator_clean

    return result.replace(
        [np.inf, -np.inf],
        np.nan,
    )


def create_domain_features(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create interpretable credit-risk features from raw application data.

    Parameters
    ----------
    data:
        Raw application feature DataFrame.

    Returns
    -------
    pd.DataFrame
        Feature-engineered copy of the input data.
    """
    data = data.copy()

    # --------------------------------------------------
    # Special-value cleaning
    # --------------------------------------------------
    special_employed_value = 365243

    data["DAYS_EMPLOYED_SPECIAL_FLAG"] = (
        data["DAYS_EMPLOYED"] == special_employed_value
    ).astype("int8")

    data["DAYS_EMPLOYED"] = data["DAYS_EMPLOYED"].replace(
        special_employed_value,
        np.nan,
    )

    # --------------------------------------------------
    # Applicant age and employment history
    # --------------------------------------------------
    data["AGE_YEARS"] = (
        -data["DAYS_BIRTH"] / 365.25
    )

    data["EMPLOYMENT_YEARS"] = (
        -data["DAYS_EMPLOYED"] / 365.25
    )

    data["REGISTRATION_YEARS"] = (
        -data["DAYS_REGISTRATION"] / 365.25
    )

    data["ID_PUBLISH_YEARS"] = (
        -data["DAYS_ID_PUBLISH"] / 365.25
    )

    data.loc[
        (data["AGE_YEARS"] < 18)
        | (data["AGE_YEARS"] > 100),
        "AGE_YEARS",
    ] = np.nan

    data.loc[
        data["EMPLOYMENT_YEARS"] < 0,
        "EMPLOYMENT_YEARS",
    ] = np.nan

    data.loc[
        data["EMPLOYMENT_YEARS"] > data["AGE_YEARS"],
        "EMPLOYMENT_YEARS",
    ] = np.nan

    # --------------------------------------------------
    # Affordability features
    # --------------------------------------------------
    data["CREDIT_INCOME_RATIO"] = safe_divide(
        data["AMT_CREDIT"],
        data["AMT_INCOME_TOTAL"],
    )

    data["ANNUITY_INCOME_RATIO"] = safe_divide(
        data["AMT_ANNUITY"],
        data["AMT_INCOME_TOTAL"],
    )

    data["CREDIT_ANNUITY_RATIO"] = safe_divide(
        data["AMT_CREDIT"],
        data["AMT_ANNUITY"],
    )

    data["INCOME_PER_PERSON"] = safe_divide(
        data["AMT_INCOME_TOTAL"],
        data["CNT_FAM_MEMBERS"],
    )

    data["CREDIT_PER_PERSON"] = safe_divide(
        data["AMT_CREDIT"],
        data["CNT_FAM_MEMBERS"],
    )

    # --------------------------------------------------
    # Loan structure features
    # --------------------------------------------------
    data["GOODS_CREDIT_RATIO"] = safe_divide(
        data["AMT_GOODS_PRICE"],
        data["AMT_CREDIT"],
    )

    data["CREDIT_GOODS_DIFFERENCE"] = (
        data["AMT_CREDIT"]
        - data["AMT_GOODS_PRICE"]
    )

    data["ANNUITY_GOODS_RATIO"] = safe_divide(
        data["AMT_ANNUITY"],
        data["AMT_GOODS_PRICE"],
    )

    # --------------------------------------------------
    # Employment stability
    # --------------------------------------------------
    data["EMPLOYMENT_AGE_RATIO"] = safe_divide(
        data["EMPLOYMENT_YEARS"],
        data["AGE_YEARS"],
    )

    # --------------------------------------------------
    # External score features
    # --------------------------------------------------
    ext_source_cols = [
        "EXT_SOURCE_1",
        "EXT_SOURCE_2",
        "EXT_SOURCE_3",
    ]

    data["EXT_SOURCE_MEAN"] = (
        data[ext_source_cols]
        .mean(axis=1)
    )

    data["EXT_SOURCE_MIN"] = (
        data[ext_source_cols]
        .min(axis=1)
    )

    data["EXT_SOURCE_MAX"] = (
        data[ext_source_cols]
        .max(axis=1)
    )

    data["EXT_SOURCE_STD"] = (
        data[ext_source_cols]
        .std(axis=1)
    )

    data["EXT_SOURCE_MISSING_COUNT"] = (
        data[ext_source_cols]
        .isna()
        .sum(axis=1)
        .astype("int8")
    )

    # --------------------------------------------------
    # Bureau inquiry features
    # --------------------------------------------------
    bureau_inquiry_cols = [
        "AMT_REQ_CREDIT_BUREAU_HOUR",
        "AMT_REQ_CREDIT_BUREAU_DAY",
        "AMT_REQ_CREDIT_BUREAU_WEEK",
        "AMT_REQ_CREDIT_BUREAU_MON",
        "AMT_REQ_CREDIT_BUREAU_QRT",
        "AMT_REQ_CREDIT_BUREAU_YEAR",
    ]

    data["BUREAU_INQUIRY_TOTAL"] = (
        data[bureau_inquiry_cols]
        .sum(axis=1, min_count=1)
    )

    recent_inquiry_cols = [
        "AMT_REQ_CREDIT_BUREAU_HOUR",
        "AMT_REQ_CREDIT_BUREAU_DAY",
        "AMT_REQ_CREDIT_BUREAU_WEEK",
        "AMT_REQ_CREDIT_BUREAU_MON",
    ]

    data["BUREAU_INQUIRY_RECENT"] = (
        data[recent_inquiry_cols]
        .sum(axis=1, min_count=1)
    )

    # --------------------------------------------------
    # Remove exact linear duplicates
    # --------------------------------------------------
    raw_time_features_to_drop = [
        "DAYS_BIRTH",
        "DAYS_EMPLOYED",
        "DAYS_REGISTRATION",
        "DAYS_ID_PUBLISH",
    ]

    data = data.drop(
        columns=raw_time_features_to_drop,
    )

    # --------------------------------------------------
    # Missingness features
    # --------------------------------------------------
    data["TOTAL_MISSING_COUNT"] = (
        data.isna()
        .sum(axis=1)
        .astype("int16")
    )

    data["TOTAL_MISSING_RATE"] = (
        data.isna()
        .mean(axis=1)
    )

    return data