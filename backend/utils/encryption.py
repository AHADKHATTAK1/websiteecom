"""
Encryption utilities for securing API keys and sensitive data
"""
from cryptography.fernet import Fernet
from django.conf import settings
import base64
import os

class EncryptionService:
    """Handle encryption and decryption of sensitive data"""
    
    def __init__(self):
        # Get or generate encryption key
        self.key = self._get_encryption_key()
        self.cipher = Fernet(self.key)
    
    def _get_encryption_key(self):
        """Get encryption key from settings or generate new one"""
        key = settings.ENCRYPTION_KEY
        if not key:
            # Generate new key
            key = Fernet.generate_key().decode()
            print(f"⚠️  Generated new encryption key: {key}")
            print("⚠️  Add this to your .env file as ENCRYPTION_KEY")
        
        if isinstance(key, str):
            key = key.encode()
        
        return key
    
    def encrypt(self, data: str) -> str:
        """Encrypt string data"""
        if not data:
            return ''
        
        encrypted = self.cipher.encrypt(data.encode())
        return base64.urlsafe_b64encode(encrypted).decode()
    
    def decrypt(self, encrypted_data: str) -> str:
        """Decrypt string data"""
        if not encrypted_data:
            return ''
        
        try:
            decoded = base64.urlsafe_b64decode(encrypted_data.encode())
            decrypted = self.cipher.decrypt(decoded)
            return decrypted.decode()
        except Exception as e:
            print(f"Decryption error: {e}")
            return ''
    
    def encrypt_dict(self, data: dict) -> dict:
        """Encrypt values in a dictionary"""
        encrypted_dict = {}
        for key, value in data.items():
            if isinstance(value, str):
                encrypted_dict[key] = self.encrypt(value)
            else:
                encrypted_dict[key] = value
        return encrypted_dict
    
    def decrypt_dict(self, encrypted_data: dict) -> dict:
        """Decrypt values in a dictionary"""
        decrypted_dict = {}
        for key, value in encrypted_data.items():
            if isinstance(value, str):
                decrypted_dict[key] = self.decrypt(value)
            else:
                decrypted_dict[key] = value
        return decrypted_dict


# Singleton instance
encryption_service = EncryptionService()
