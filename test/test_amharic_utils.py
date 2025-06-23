"""
Tests for Amharic text processing utilities.

This module contains comprehensive tests for the AmharicTextProcessor
class and related utility functions.
"""

import pytest
from src.utils.amharic_utils import AmharicTextProcessor


class TestAmharicTextProcessor:
    """Test cases for AmharicTextProcessor class."""
    
    @pytest.fixture
    def processor(self):
        """Create a processor instance for testing."""
        return AmharicTextProcessor()
    
    def test_initialization(self, processor):
        """Test processor initialization."""
        assert processor is not None
        assert len(processor.amharic_chars) > 0
        assert len(processor.price_patterns) > 0
        assert len(processor.location_patterns) > 0
        assert len(processor.product_patterns) > 0
    
    def test_amharic_ratio_calculation(self, processor):
        """Test Amharic ratio calculation."""
        # Pure Amharic text
        amharic_text = "ስልክ አዲስ አበባ ውስጥ 5000 ብር ዋጋ አለው"
        ratio = processor.get_amharic_ratio(amharic_text)
        assert 0.8 <= ratio <= 1.0
        
        # Mixed text
        mixed_text = "Phone in Addis Ababa costs 5000 birr"
        ratio = processor.get_amharic_ratio(mixed_text)
        assert 0.0 <= ratio <= 0.3
        
        # Empty text
        ratio = processor.get_amharic_ratio("")
        assert ratio == 0.0
    
    def test_amharic_dominant_detection(self, processor):
        """Test Amharic dominant text detection."""
        amharic_text = "ስልክ አዲስ አበባ ውስጥ"
        assert processor.is_amharic_dominant(amharic_text, threshold=0.3)
        
        english_text = "Phone in Addis Ababa"
        assert not processor.is_amharic_dominant(english_text, threshold=0.3)
    
    def test_text_normalization(self, processor):
        """Test Amharic text normalization."""
        # Test basic normalization
        text = "ስልክ   አዲስ   አበባ"
        normalized = processor.normalize_amharic_text(text)
        assert "  " not in normalized
        
        # Test typo correction
        text_with_typo = "ያለዉ ነው"
        normalized = processor.normalize_amharic_text(text_with_typo)
        assert "ያለዉ" not in normalized
    
    def test_text_cleaning(self, processor):
        """Test text cleaning functionality."""
        # Test with emojis
        text_with_emojis = "ስልክ 📱 አዲስ 🏙️ አበባ"
        cleaned = processor.clean_text(text_with_emojis, remove_emojis=True)
        assert "📱" not in cleaned
        assert "🏙️" not in cleaned
        
        # Test with URLs
        text_with_urls = "ስልክ አዲስ አበባ https://example.com ውስጥ"
        cleaned = processor.clean_text(text_with_urls, remove_urls=True)
        assert "https://example.com" not in cleaned
        
        # Test phone number removal
        text_with_phone = "ስልክ 0912345678 አዲስ አበባ"
        cleaned = processor.clean_text(text_with_phone, remove_phone_numbers=True)
        assert "0912345678" not in cleaned
    
    def test_price_extraction(self, processor):
        """Test price extraction from text."""
        # Test Ethiopian Birr
        text_with_birr = "ስልክ 5000 ብር ዋጋ አለው"
        prices = processor.extract_prices(text_with_birr)
        assert len(prices) > 0
        assert prices[0]['value'] == '5000'
        assert prices[0]['currency'] == 'ETB'
        
        # Test dollar
        text_with_dollar = "Phone costs 100 dollar"
        prices = processor.extract_prices(text_with_dollar)
        assert len(prices) > 0
        assert prices[0]['currency'] == 'USD'
        
        # Test range
        text_with_range = "Price 1000-2000 birr"
        prices = processor.extract_prices(text_with_range)
        assert len(prices) > 0
    
    def test_location_extraction(self, processor):
        """Test location extraction from text."""
        text_with_location = "ስልክ አዲስ አበባ ውስጥ ያለ"
        locations = processor.extract_locations(text_with_location)
        assert len(locations) > 0
        assert any('አዲስ አበባ' in loc['name'] for loc in locations)
    
    def test_product_extraction(self, processor):
        """Test product extraction from text."""
        text_with_product = "ስልክ አዲስ አበባ ውስጥ"
        products = processor.extract_products(text_with_product)
        assert len(products) > 0
        assert any('ስልክ' in prod['name'] for prod in products)
    
    def test_entity_categorization(self, processor):
        """Test product categorization."""
        assert processor._categorize_product("ስልክ") == "electronics"
        assert processor._categorize_product("ልብስ") == "fashion"
        assert processor._categorize_product("መጽሐፍ") == "books"
        assert processor._categorize_product("unknown") == "other"
    
    def test_currency_detection(self, processor):
        """Test currency detection."""
        assert processor._detect_currency("5000 ብር") == "ETB"
        assert processor._detect_currency("100 dollar") == "USD"
        assert processor._detect_currency("5000") == "UNKNOWN"
    
    def test_comprehensive_entity_extraction(self, processor):
        """Test comprehensive entity extraction."""
        text = "ስልክ አዲስ አበባ ውስጥ 5000 ብር ዋጋ አለው"
        entities = processor.extract_all_entities(text)
        
        assert 'prices' in entities
        assert 'locations' in entities
        assert 'products' in entities
        
        assert len(entities['prices']) > 0
        assert len(entities['locations']) > 0
        assert len(entities['products']) > 0
    
    def test_text_statistics(self, processor):
        """Test text statistics generation."""
        text = "ስልክ አዲስ አበባ ውስጥ 5000 ብር ዋጋ አለው"
        stats = processor.get_text_statistics(text)
        
        assert 'total_characters' in stats
        assert 'total_words' in stats
        assert 'amharic_ratio' in stats
        assert 'entity_counts' in stats
        assert 'is_amharic_dominant' in stats
        
        assert stats['total_characters'] > 0
        assert stats['total_words'] > 0
        assert 0.0 <= stats['amharic_ratio'] <= 1.0
        assert isinstance(stats['is_amharic_dominant'], bool)


def test_process_text_batch():
    """Test batch text processing."""
    from src.utils.amharic_utils import process_text_batch
    
    texts = [
        "ስልክ አዲስ አበባ ውስጥ",
        "Phone in Addis Ababa",
        "ስልክ 5000 ብር ዋጋ አለው"
    ]
    
    df = process_text_batch(texts)
    
    assert len(df) == 3
    assert 'amharic_ratio' in df.columns
    assert 'is_amharic_dominant' in df.columns
    assert 'entity_counts' in df.columns


if __name__ == "__main__":
    pytest.main([__file__]) 