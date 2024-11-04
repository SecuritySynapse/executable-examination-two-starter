"""Confirm the correctness of functions in question_two."""

import pytest

# ruff: noqa: PLR2004
from questions.question_two import (
    apply_decryption_methods,
    apply_encryption_methods,
    decrypt_atbash_cipher,
    decrypt_transposition_cipher,
    encrypt_atbash_cipher,
    encrypt_transposition_cipher,
    rot13_decrypt,
    rot13_encrypt,
)


@pytest.mark.question_two_part_a
def test_encrypt_atbash_cipher():
    """Confirm correctness of question part."""
    assert (
        encrypt_atbash_cipher("ABC") == "ZYX"
    ), "Failed to shift forwards uppercase letters"
    assert (
        encrypt_atbash_cipher("abc") == "zyx"
    ), "Failed to shift forwards lowercase letters"
    assert (
        encrypt_atbash_cipher("XYZ") == "CBA"
    ), "Failed to shift backwards uppercase letters"
    assert (
        encrypt_atbash_cipher("xyz") == "cba"
    ), "Failed to wrap around lowercase letters"
    assert (
        encrypt_atbash_cipher("AbC") == "ZyX"
    ), "Failed to shift forwards mixed case letters"
    assert (
        encrypt_atbash_cipher("ZyX") == "AbC"
    ), "Failed to shift backwards mixed case letters"


@pytest.mark.question_two_part_a
def test_decrypt_atbash_cipher():
    """Confirm correctness of question part."""
    assert (
        decrypt_atbash_cipher("ABC") == "ZYX"
    ), "Failed to shift forwards uppercase letters"
    assert (
        decrypt_atbash_cipher("abc") == "zyx"
    ), "Failed to shift forwards lowercase letters"
    assert (
        decrypt_atbash_cipher("XYZ") == "CBA"
    ), "Failed to shift backwards uppercase letters"
    assert (
        decrypt_atbash_cipher("xyz") == "cba"
    ), "Failed to wrap around lowercase letters"
    assert (
        decrypt_atbash_cipher("AbC") == "ZyX"
    ), "Failed to shift forwards mixed case letters"
    assert (
        decrypt_atbash_cipher("ZyX") == "AbC"
    ), "Failed to shift backwards mixed case letters"


@pytest.mark.question_two_part_b
def test_encrypt_transposition_cipher():
    """Test for a question part."""
    assert (
        encrypt_transposition_cipher(8, "Common sense is not so common.")
        == "Cenoonommstmme oo snnio. s s c"
    ), "Encryption failed for key 8 and the common sense message"


@pytest.mark.question_two_part_b
def test_decrypt_transposition_cipher():
    """Test for a question part."""
    assert (
        decrypt_transposition_cipher(8, "Cenoonommstmme oo snnio. s s c")
        == "Common sense is not so common."
    ), "Decryption failed for key 8 and the common sense message"


@pytest.mark.question_two_part_c
def test_rot13_encrypt():
    """Test the ROT13 encryption function."""
    assert rot13_encrypt("abc") == "nop", "Encrypt: Failed to shift lowercase letters"
    assert rot13_encrypt("ABC") == "NOP", "Encrypt: Failed to shift uppercase letters"
    assert (
        rot13_encrypt("nop") == "abc"
    ), "Encrypt: Failed to wrap around lowercase letters"
    assert (
        rot13_encrypt("NOP") == "ABC"
    ), "Encrypt: Failed to wrap around uppercase letters"
    assert rot13_encrypt("AbC") == "NoP", "Encrypt: Failed to handle mixed case letters"
    assert (
        rot13_encrypt("123") == "123"
    ), "Encrypt: Failed to ignore non-alphabetic characters of numbers"
    assert (
        rot13_encrypt("%$#") == "%$#"
    ), "Encrypt: Failed to ignore non-alphabetic characters of punctuation"


@pytest.mark.question_two_part_c
def test_rot13_decrypt():
    """Test the ROT13 decryption function."""
    assert rot13_decrypt("nop") == "abc", "Decrypt: Failed to shift lowercase letters"
    assert rot13_decrypt("NOP") == "ABC", "Decrypt: Failed to shift uppercase letters"
    assert (
        rot13_decrypt("abc") == "nop"
    ), "Decrypt: Failed to wrap around lowercase letters"
    assert (
        rot13_decrypt("ABC") == "NOP"
    ), "Decrypt: Failed to wrap around uppercase letters"
    assert rot13_decrypt("NoP") == "AbC", "Decrypt: Failed to handle mixed case letters"
    assert (
        rot13_decrypt("123") == "123"
    ), "Decrypt: Failed to ignore non-alphabetic characters of numbers"
    assert (
        rot13_decrypt("%$#") == "%$#"
    ), "Decrypt: Failed to ignore non-alphabetic characters of punctuation"


@pytest.mark.question_two_part_d
def test_apply_encryption_methods_singleton_list():
    """Test the application of multiple encryption methods."""
    plaintext = "abc"
    expected_ciphertext = "nop"
    encryption_functions = [rot13_encrypt]
    result = apply_encryption_methods(encryption_functions, plaintext)
    assert (
        result == expected_ciphertext
    ), f"Expected {expected_ciphertext} but got {result} after applying ROT13"
    plaintext = "nop"
    expected_ciphertext = "mlk"
    encryption_functions = [encrypt_atbash_cipher]
    result = apply_encryption_methods(encryption_functions, plaintext)
    assert (
        result == expected_ciphertext
    ), f"Expected {expected_ciphertext} but got {result} after applying Atbash"


@pytest.mark.question_two_part_d
def test_apply_encryption_methods_combined_list():
    """Test the application of multiple encryption methods."""
    plaintext = "abc"
    expected_ciphertext = "mlk"
    encryption_functions = [rot13_encrypt, encrypt_atbash_cipher]
    result = apply_encryption_methods(encryption_functions, plaintext)
    assert (
        result == expected_ciphertext
    ), f"Expected {expected_ciphertext} but got {result} after applying Atbash+ROT13"


@pytest.mark.question_two_part_d
def test_apply_decryption_methods_singleton_list():
    """Test the application of multiple decryption methods."""
    ciphertext = "nop"
    expected_plaintext = "abc"
    decryption_functions = [rot13_encrypt]  # ROT13 is its own inverse
    result = apply_decryption_methods(decryption_functions, ciphertext)
    assert (
        result == expected_plaintext
    ), f"Expected {expected_plaintext} but got {result} after applying ROT13"
    ciphertext = "mlk"
    expected_plaintext = "nop"
    decryption_functions = [encrypt_atbash_cipher]  # Atbash is its own inverse
    result = apply_decryption_methods(decryption_functions, ciphertext)
    assert (
        result == expected_plaintext
    ), f"Expected {expected_plaintext} but got {result} after applying Atbash"


@pytest.mark.question_two_part_d
def test_apply_decryption_methods_combined_list():
    """Test the application of multiple decryption methods."""
    ciphertext = "mlk"
    expected_plaintext = "abc"
    decryption_functions = [
        encrypt_atbash_cipher,
        rot13_encrypt,
    ]  # Reverse order of encryption
    result = apply_decryption_methods(decryption_functions, ciphertext)
    assert (
        result == expected_plaintext
    ), f"Expected {expected_plaintext} but got {result} after applying Atbash+ROT13"
