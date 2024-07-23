from . import BaseModel, Optional, Union, Dict

class DailyCipher(BaseModel):
    error: Optional[str] = None
    bonusCoins: Optional[int] = None
    isClaimed: Optional[bool] = None
    remainSeconds: Optional[int] = None

    @classmethod
    def mixed_dict(cls, data: Union[Dict, None]):
        if "dailyCipher" in data:
            daily_cipher_data = data["dailyCipher"]
        else:
            daily_cipher_data = data
        
        return cls(**daily_cipher_data)