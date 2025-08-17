"""
Core AI Engine for DisciplineCall.ai
Supports both cloud (OpenAI) and local (open-source) models
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class AIProvider(Enum):
    """Supported AI providers for conversation"""
    OPENAI = "openai"
    LOCAL = "local"
    ANTHROPIC = "anthropic"


class PersonalityMode(Enum):
    """Different coaching personality modes"""
    MOTIVATOR = "motivator"
    DRILL_SERGEANT = "drill_sergeant"
    ABUSER = "abuser"
    FRIEND = "friend"
    MENTOR = "mentor"


class BaseAIEngine(ABC):
    """Abstract base class for AI conversation engines"""
    
    def __init__(self, personality: PersonalityMode = PersonalityMode.MOTIVATOR):
        self.personality = personality
        self.conversation_history: List[Dict[str, Any]] = []
    
    @abstractmethod
    async def generate_response(
        self,
        user_input: str,
        context: Dict[str, Any],
        call_type: str = "morning"
    ) -> str:
        """Generate AI response based on user input and context"""
        pass
    
    @abstractmethod
    async def analyze_metrics(
        self,
        metrics: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Analyze user metrics and provide insights"""
        pass


class CloudAIEngine(BaseAIEngine):
    """Cloud-based AI engine using OpenAI GPT models"""
    
    def __init__(self, api_key: str, model: str = "gpt-4o", **kwargs):
        super().__init__(**kwargs)
        self.api_key = api_key
        self.model = model
        # Initialize OpenAI client here
    
    async def generate_response(
        self,
        user_input: str,
        context: Dict[str, Any],
        call_type: str = "morning"
    ) -> str:
        """Generate response using OpenAI models"""
        
        system_prompt = self._get_personality_prompt()
        user_context = self._format_context(context, call_type)
        
        # TODO: Implement OpenAI API call
        # messages = [
        #     {"role": "system", "content": system_prompt},
        #     {"role": "user", "content": f"{user_context}\nUser: {user_input}"}
        # ]
        
        logger.info(f"Generating {call_type} response for personality: {self.personality}")
        return f"AI Response for {call_type} call (Cloud mode)"
    
    async def analyze_metrics(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze metrics using cloud AI"""
        # TODO: Implement metrics analysis
        return {"insights": "Cloud-based analysis", "recommendations": []}


class LocalAIEngine(BaseAIEngine):
    """Local AI engine using open-source models"""
    
    def __init__(self, model_path: str = "llama2", **kwargs):
        super().__init__(**kwargs)
        self.model_path = model_path
        # Initialize local model here (Ollama, Llama.cpp, etc.)
    
    async def generate_response(
        self,
        user_input: str,
        context: Dict[str, Any],
        call_type: str = "morning"
    ) -> str:
        """Generate response using local models"""
        
        system_prompt = self._get_personality_prompt()
        user_context = self._format_context(context, call_type)
        
        # TODO: Implement local model inference
        logger.info(f"Generating {call_type} response locally for personality: {self.personality}")
        return f"AI Response for {call_type} call (Local mode)"
    
    async def analyze_metrics(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze metrics using local AI"""
        # TODO: Implement local metrics analysis
        return {"insights": "Local analysis", "recommendations": []}


class AIEngineFactory:
    """Factory for creating AI engines based on configuration"""
    
    @staticmethod
    def create_engine(
        provider: AIProvider,
        personality: PersonalityMode = PersonalityMode.MOTIVATOR,
        **kwargs
    ) -> BaseAIEngine:
        """Create appropriate AI engine based on provider"""
        
        if provider == AIProvider.OPENAI:
            return CloudAIEngine(personality=personality, **kwargs)
        elif provider == AIProvider.LOCAL:
            return LocalAIEngine(personality=personality, **kwargs)
        else:
            raise ValueError(f"Unsupported AI provider: {provider}")


# Personality prompts for different coaching styles
PERSONALITY_PROMPTS = {
    PersonalityMode.MOTIVATOR: """
    You are an enthusiastic, positive personal coach. You're supportive, encouraging, 
    and always see the bright side. You celebrate small wins and help users stay motivated.
    Use phrases like "You've got this!", "Amazing progress!", "Let's tackle this together!"
    """,
    
    PersonalityMode.DRILL_SERGEANT: """
    You are a strict, no-nonsense drill sergeant coach. You demand excellence, 
    don't accept excuses, and push users to their limits. You're tough but fair.
    Use phrases like "NO EXCUSES!", "Drop and give me 20!", "You're better than this!"
    """,
    
    PersonalityMode.ABUSER: """
    You are a sarcastic, brutally honest coach who uses humor and gentle insults 
    to motivate. You're like a friend who calls you out on your BS with love.
    Use phrases like "Really? That's your excuse?", "I've seen vegetables with more discipline", 
    but always end with genuine encouragement.
    """,
    
    PersonalityMode.FRIEND: """
    You are a caring, understanding friend who provides gentle accountability. 
    You're empathetic, patient, and always ready to listen and support.
    Use phrases like "I understand", "That's totally normal", "We all have tough days"
    """,
    
    PersonalityMode.MENTOR: """
    You are a wise, experienced mentor who provides thoughtful guidance and insights. 
    You ask probing questions and help users discover their own solutions.
    Use phrases like "What do you think would help?", "Consider this perspective", "In my experience"
    """
}
