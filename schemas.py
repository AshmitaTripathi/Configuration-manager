from pydantic import BaseModel

class ConfigurationCreate(BaseModel):
    country_code: str
    business_name: str
    pan: str
    gstin: str
    # Add more fields for other country-specific requirements

class ConfigurationRead(BaseModel):
    id: int
    country_code: str
    business_name: str
    pan: str
    gstin: str
    # Add more fields for other country-specific requirements

class ConfigurationUpdate(BaseModel):
    country_code: str
    business_name: str
    pan: str
    gstin: str
    # Add more fields for other country-specific requirements