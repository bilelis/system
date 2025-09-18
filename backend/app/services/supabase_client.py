"""
Supabase Client Service for Hotel Management System
هذا الفايل يدير الاتصال مع Supabase باستخدام Service Role Key
"""

from supabase import create_client, Client
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class SupabaseService:
    """
    Service for managing Supabase connections and operations
    """
    
    def __init__(self):
        self.supabase: Client = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize Supabase client with fallback handling"""
        try:
            # Check if we have valid Supabase credentials
            if not settings.SUPABASE_URL or settings.SUPABASE_URL == "your-supabase-url":
                logger.warning("Supabase URL not configured, skipping Supabase client initialization")
                self.supabase = None
                return
                
            # Try Service Role Key first
            service_key = settings.SUPABASE_SERVICE_ROLE_KEY
            if service_key and service_key != "your-service-role-key-here":
                try:
                    self.supabase = create_client(
                        supabase_url=settings.SUPABASE_URL,
                        supabase_key=service_key
                    )
                    logger.info("Supabase client initialized with Service Role Key")
                    return
                except Exception as e:
                    logger.warning(f"Service Role Key failed: {e}")
            
            # Fallback to Anon Key for basic operations
            anon_key = settings.SUPABASE_ANON_KEY
            if anon_key and anon_key != "your-supabase-anon-key":
                try:
                    self.supabase = create_client(
                        supabase_url=settings.SUPABASE_URL,
                        supabase_key=anon_key
                    )
                    logger.info("Supabase client initialized with Anon Key (limited permissions)")
                    return
                except Exception as e:
                    logger.warning(f"Anon Key failed: {e}")
            
            # If both fail, disable Supabase integration
            logger.warning("No valid Supabase credentials found, disabling Supabase integration")
            self.supabase = None
            
        except Exception as e:
            logger.error(f"Failed to initialize Supabase client: {e}")
            self.supabase = None
    
    def get_client(self) -> Client:
        """Get the Supabase client instance"""
        if not self.supabase:
            self._initialize_client()
        return self.supabase
    
    def is_available(self) -> bool:
        """Check if Supabase client is available"""
        return self.supabase is not None
    
    async def test_connection(self) -> bool:
        """Test the Supabase connection"""
        if not self.supabase:
            logger.warning("Supabase client not available")
            return False
            
        try:
            # Test with a simple query to users table
            response = self.supabase.table('users').select('id').limit(1).execute()
            return response.data is not None
        except Exception as e:
            logger.error(f"Supabase connection test failed: {e}")
            return False

# Global instance
supabase_service = SupabaseService()