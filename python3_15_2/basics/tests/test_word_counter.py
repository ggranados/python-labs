from app.exercises.word_counter import count_words

def test_count_words():
    assert count_words("Hello world") == 2
    assert count_words("This is a test") == 4
    assert count_words("") == 0
    assert count_words("One") == 1
    assert count_words("Two words here") == 3
    assert count_words("Multiple    spaces") == 2
    assert count_words(" Leading and trailing ") == 3
    assert count_words("Punctuation, should not affect!") == 4
    assert count_words("New\nline and\ttab") == 4
    assert count_words("Special characters #$%^&*()") == 2
    print("All tests passed!")