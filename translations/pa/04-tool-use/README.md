<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7d24f735b3c326b2e515f049a0330e54",
  "translation_date": "2025-08-21T12:50:08+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "pa"
}
-->
[![ਚੰਗੇ AI ਏਜੰਟਾਂ ਨੂੰ ਡਿਜ਼ਾਈਨ ਕਰਨ ਦਾ ਤਰੀਕਾ](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.pa.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ਉਪਰ ਦਿੱਤੀ ਤਸਵੀਰ 'ਤੇ ਕਲਿਕ ਕਰਕੇ ਇਸ ਪਾਠ ਦਾ ਵੀਡੀਓ ਵੇਖੋ)_

# ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ

ਟੂਲ ਦਿਲਚਸਪ ਹਨ ਕਿਉਂਕਿ ਇਹ AI ਏਜੰਟਾਂ ਨੂੰ ਵਿਆਪਕ ਸਮਰੱਥਾਵਾਂ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ। ਏਜੰਟ ਦੇ ਕੁਝ ਸੀਮਿਤ ਕਾਰਵਾਈਆਂ ਕਰਨ ਦੀ ਥਾਂ, ਟੂਲ ਸ਼ਾਮਲ ਕਰਕੇ, ਏਜੰਟ ਹੁਣ ਵੱਖ-ਵੱਖ ਕਾਰਵਾਈਆਂ ਕਰ ਸਕਦਾ ਹੈ। ਇਸ ਅਧਿਆਇ ਵਿੱਚ, ਅਸੀਂ ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਦੇਖਾਂਗੇ, ਜੋ ਵੇਰਵਾ ਦਿੰਦਾ ਹੈ ਕਿ AI ਏਜੰਟ ਆਪਣੇ ਲਕਸ਼ਾਂ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਖਾਸ ਟੂਲਾਂ ਨੂੰ ਕਿਵੇਂ ਵਰਤ ਸਕਦੇ ਹਨ।

## ਪਰਿਚਯ

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਲੱਭਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਰਹੇ ਹਾਂ:

- ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਕੀ ਹੈ?
- ਇਹ ਕਿਹੜੇ ਉਪਯੋਗ ਮਾਮਲਿਆਂ 'ਤੇ ਲਾਗੂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ?
- ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਨੂੰ ਲਾਗੂ ਕਰਨ ਲਈ ਕਿਹੜੇ ਤੱਤ/ਬਿਲਡਿੰਗ ਬਲਾਕਾਂ ਦੀ ਲੋੜ ਹੈ?
- ਭਰੋਸੇਯੋਗ AI ਏਜੰਟਾਂ ਬਣਾਉਣ ਲਈ ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਵਿਸ਼ੇਸ਼ ਵਿਚਾਰ ਕੀ ਹਨ?

## ਸਿੱਖਣ ਦੇ ਲਕਸ਼

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਇਹ ਕਰਨ ਦੇ ਯੋਗ ਹੋਵੋਗੇ:

- ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਅਤੇ ਇਸਦਾ ਉਦੇਸ਼ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ।
- ਉਹ ਉਪਯੋਗ ਮਾਮਲੇ ਪਛਾਣੋ ਜਿੱਥੇ ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਲਾਗੂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।
- ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਨੂੰ ਲਾਗੂ ਕਰਨ ਲਈ ਜ਼ਰੂਰੀ ਮੁੱਖ ਤੱਤਾਂ ਨੂੰ ਸਮਝੋ।
- ਇਸ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਦੀ ਵਰਤੋਂ ਕਰਦੇ AI ਏਜੰਟਾਂ ਵਿੱਚ ਭਰੋਸੇਯੋਗਤਾ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਵਿਚਾਰਾਂ ਨੂੰ ਪਛਾਣੋ।

## ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਕੀ ਹੈ?

**ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ** LLMs ਨੂੰ ਖਾਸ ਟੂਲਾਂ ਨਾਲ ਸੰਚਾਰ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਦੇਣ 'ਤੇ ਧਿਆਨ ਕੇਂਦ੍ਰਿਤ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ ਖਾਸ ਲਕਸ਼ਾਂ ਨੂੰ ਪੂਰਾ ਕੀਤਾ ਜਾ ਸਕੇ। ਟੂਲ ਉਹ ਕੋਡ ਹੁੰਦੇ ਹਨ ਜੋ ਏਜੰਟ ਦੁਆਰਾ ਕਾਰਵਾਈਆਂ ਕਰਨ ਲਈ ਚਲਾਏ ਜਾ ਸਕਦੇ ਹਨ। ਟੂਲ ਇੱਕ ਸਧਾਰਨ ਫੰਕਸ਼ਨ ਹੋ ਸਕਦਾ ਹੈ ਜਿਵੇਂ ਕਿ ਕੈਲਕੁਲੇਟਰ, ਜਾਂ ਕਿਸੇ ਤੀਜੀ ਪਾਰਟੀ ਸੇਵਾ ਲਈ API ਕਾਲ ਜਿਵੇਂ ਕਿ ਸਟਾਕ ਕੀਮਤ ਜਾਂ ਮੌਸਮ ਦੀ ਪੇਸ਼ਗੋਈ। AI ਏਜੰਟਾਂ ਦੇ ਸੰਦਰਭ ਵਿੱਚ, ਟੂਲ **ਮਾਡਲ-ਜਨਰੇਟ ਕੀਤੇ ਫੰਕਸ਼ਨ ਕਾਲਾਂ** ਦੇ ਜਵਾਬ ਵਿੱਚ ਚਲਾਏ ਜਾਣ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

## ਇਹ ਕਿਹੜੇ ਉਪਯੋਗ ਮਾਮਲਿਆਂ 'ਤੇ ਲਾਗੂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ?

AI ਏਜੰਟ ਟੂਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜਟਿਲ ਕੰਮ ਪੂਰੇ ਕਰ ਸਕਦੇ ਹਨ, ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਨ, ਜਾਂ ਫੈਸਲੇ ਲੈ ਸਕਦੇ ਹਨ। ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਅਕਸਰ ਬਾਹਰੀ ਸਿਸਟਮਾਂ ਨਾਲ ਗਤੀਸ਼ੀਲ ਸੰਚਾਰ ਦੀ ਲੋੜ ਵਾਲੇ ਦ੍ਰਿਸ਼ਾਂ ਵਿੱਚ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਡਾਟਾਬੇਸ, ਵੈੱਬ ਸੇਵਾਵਾਂ, ਜਾਂ ਕੋਡ ਇੰਟਰਪ੍ਰੀਟਰ। ਇਹ ਸਮਰੱਥਾ ਕਈ ਵੱਖ-ਵੱਖ ਉਪਯੋਗ ਮਾਮਲਿਆਂ ਲਈ ਲਾਭਦਾਇਕ ਹੈ, ਜਿਵੇਂ:

- **ਗਤੀਸ਼ੀਲ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤੀ:** ਏਜੰਟ ਬਾਹਰੀ APIs ਜਾਂ ਡਾਟਾਬੇਸਾਂ ਨੂੰ ਪੁੱਛ ਸਕਦੇ ਹਨ ਤਾਂ ਜੋ ਤਾਜ਼ਾ ਡਾਟਾ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾ ਸਕੇ (ਜਿਵੇਂ ਕਿ SQLite ਡਾਟਾਬੇਸ ਨੂੰ ਡਾਟਾ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ ਪੁੱਛਣਾ, ਸਟਾਕ ਕੀਮਤਾਂ ਜਾਂ ਮੌਸਮ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨਾ)।
- **ਕੋਡ ਚਲਾਉਣਾ ਅਤੇ ਵਿਆਖਿਆ:** ਏਜੰਟ ਗਣਿਤ ਸਮੱਸਿਆਵਾਂ ਹੱਲ ਕਰਨ, ਰਿਪੋਰਟਾਂ ਬਣਾਉਣ, ਜਾਂ ਸਿਮੂਲੇਸ਼ਨ ਕਰਨ ਲਈ ਕੋਡ ਜਾਂ ਸਕ੍ਰਿਪਟ ਚਲਾ ਸਕਦੇ ਹਨ।
- **ਵਰਕਫਲੋ ਆਟੋਮੇਸ਼ਨ:** ਟਾਸਕ ਸ਼ੈਡਿਊਲਰ, ਈਮੇਲ ਸੇਵਾਵਾਂ, ਜਾਂ ਡਾਟਾ ਪਾਈਪਲਾਈਨ ਵਰਗੇ ਟੂਲਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਕੇ ਦੁਹਰਾਏ ਜਾਂ ਬਹੁ-ਕਦਮ ਵਾਲੇ ਵਰਕਫਲੋਜ਼ ਨੂੰ ਆਟੋਮੇਟ ਕਰਨਾ।
- **ਗਾਹਕ ਸਹਾਇਤਾ:** ਏਜੰਟ CRM ਸਿਸਟਮਾਂ, ਟਿਕਟਿੰਗ ਪਲੇਟਫਾਰਮਾਂ, ਜਾਂ ਨੋਲਿਜ ਬੇਸਾਂ ਨਾਲ ਸੰਚਾਰ ਕਰਕੇ ਉਪਭੋਗਤਾ ਦੀਆਂ ਪੁੱਛਗਿੱਛਾਂ ਦਾ ਹੱਲ ਕਰ ਸਕਦੇ ਹਨ।
- **ਸਮੱਗਰੀ ਬਣਾਉਣਾ ਅਤੇ ਸੰਪਾਦਨ:** ਏਜੰਟ ਗ੍ਰਾਮਰ ਚੈੱਕਰ, ਟੈਕਸਟ ਸੰਖੇਪਕ, ਜਾਂ ਸਮੱਗਰੀ ਸੁਰੱਖਿਆ ਮੁਲਾਂਕਨ ਕਰਨ ਵਾਲੇ ਟੂਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਮੱਗਰੀ ਬਣਾਉਣ ਦੇ ਕੰਮਾਂ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰ ਸਕਦੇ ਹਨ।

## ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਨੂੰ ਲਾਗੂ ਕਰਨ ਲਈ ਕਿਹੜੇ ਤੱਤ/ਬਿਲਡਿੰਗ ਬਲਾਕਾਂ ਦੀ ਲੋੜ ਹੈ?

ਇਹ ਬਿਲਡਿੰਗ ਬਲਾਕ AI ਏਜੰਟ ਨੂੰ ਵਿਆਪਕ ਕੰਮ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਦਿੰਦੇ ਹਨ। ਆਓ ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਨੂੰ ਲਾਗੂ ਕਰਨ ਲਈ ਜ਼ਰੂਰੀ ਮੁੱਖ ਤੱਤਾਂ 'ਤੇ ਨਜ਼ਰ ਮਾਰਦੇ ਹਾਂ:

- **ਫੰਕਸ਼ਨ/ਟੂਲ ਸਕੀਮਾਂ:** ਉਪਲਬਧ ਟੂਲਾਂ ਦੀ ਵਿਸਥਾਰਿਤ ਪਰਿਭਾਸ਼ਾ, ਜਿਸ ਵਿੱਚ ਫੰਕਸ਼ਨ ਦਾ ਨਾਮ, ਉਦੇਸ਼, ਲੋੜੀਂਦੇ ਪੈਰਾਮੀਟਰ, ਅਤੇ ਉਮੀਦ ਕੀਤੇ ਨਤੀਜੇ ਸ਼ਾਮਲ ਹਨ। ਇਹ ਸਕੀਮਾਂ LLM ਨੂੰ ਸਮਝਣ ਯੋਗ ਬਣਾਉਂਦੀਆਂ ਹਨ ਕਿ ਕਿਹੜੇ ਟੂਲ ਉਪਲਬਧ ਹਨ ਅਤੇ ਵੈਧ ਬੇਨਤੀਆਂ ਕਿਵੇਂ ਬਣਾਈਆਂ ਜਾਣ।
- **ਫੰਕਸ਼ਨ ਚਲਾਉਣ ਦੀ ਤਰਕ:** ਇਹ ਗਵਰਨ ਕਰਦਾ ਹੈ ਕਿ ਟੂਲਾਂ ਨੂੰ ਕਿਵੇਂ ਅਤੇ ਕਦੋਂ ਵਰਤਿਆ ਜਾਵੇ, ਉਪਭੋਗਤਾ ਦੇ ਇਰਾਦੇ ਅਤੇ ਗੱਲਬਾਤ ਦੇ ਸੰਦਰਭ ਦੇ ਅਧਾਰ 'ਤੇ। ਇਸ ਵਿੱਚ ਪਲਾਨਰ ਮੋਡੀਊਲ, ਰੂਟਿੰਗ ਮਕੈਨਿਜ਼ਮ, ਜਾਂ ਸ਼ਰਤਾਂ ਵਾਲੇ ਫਲੋ ਸ਼ਾਮਲ ਹੋ ਸਕਦੇ ਹਨ ਜੋ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ ਟੂਲ ਵਰਤੋਂ ਦਾ ਨਿਰਧਾਰਨ ਕਰਦੇ ਹਨ।
- **ਸੰਦੇਸ਼ ਸੰਭਾਲਣ ਸਿਸਟਮ:** ਉਹ ਘਟਕ ਜੋ ਉਪਭੋਗਤਾ ਦੇ ਇਨਪੁਟ, LLM ਦੇ ਜਵਾਬ, ਟੂਲ ਕਾਲਾਂ, ਅਤੇ ਟੂਲ ਨਤੀਜਿਆਂ ਦੇ ਵਿਚਕਾਰ ਗੱਲਬਾਤ ਦੇ ਫਲੋ ਨੂੰ ਸੰਭਾਲਦੇ ਹਨ।
- **ਟੂਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਫਰੇਮਵਰਕ:** ਢਾਂਚਾ ਜੋ ਏਜੰਟ ਨੂੰ ਵੱਖ-ਵੱਖ ਟੂਲਾਂ ਨਾਲ ਜੋੜਦਾ ਹੈ, ਚਾਹੇ ਉਹ ਸਧਾਰਨ ਫੰਕਸ਼ਨ ਹੋਣ ਜਾਂ ਜਟਿਲ ਬਾਹਰੀ ਸੇਵਾਵਾਂ।
- **ਗਲਤੀ ਸੰਭਾਲਣ ਅਤੇ ਵੈਧਤਾ:** ਟੂਲ ਚਲਾਉਣ ਵਿੱਚ ਅਸਫਲਤਾਵਾਂ ਨੂੰ ਸੰਭਾਲਣ, ਪੈਰਾਮੀਟਰਾਂ ਦੀ ਵੈਧਤਾ, ਅਤੇ ਅਣਅਪੇक्षित ਜਵਾਬਾਂ ਨੂੰ ਸੰਭਾਲਣ ਦੇ ਮਕੈਨਿਜ਼ਮ।
- **ਸਟੇਟ ਮੈਨੇਜਮੈਂਟ:** ਗੱਲਬਾਤ ਦੇ ਸੰਦਰਭ, ਪਿਛਲੇ ਟੂਲ ਸੰਚਾਰ, ਅਤੇ ਲਗਾਤਾਰ ਡਾਟਾ ਨੂੰ ਟ੍ਰੈਕ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ ਬਹੁ-ਟਰਨ ਗੱਲਬਾਤਾਂ ਵਿੱਚ ਸਥਿਰਤਾ ਯਕੀਨੀ ਬਣਾਈ ਜਾ ਸਕੇ।

ਅਗਲੇ ਹਿੱਸੇ ਵਿੱਚ, ਅਸੀਂ ਫੰਕਸ਼ਨ/ਟੂਲ ਕਾਲਿੰਗ ਨੂੰ ਵਿਸਥਾਰ ਵਿੱਚ ਦੇਖਾਂਗੇ।

### ਫੰਕਸ਼ਨ/ਟੂਲ ਕਾਲਿੰਗ

ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ (LLMs) ਨੂੰ ਟੂਲਾਂ ਨਾਲ ਸੰਚਾਰ ਕਰਨ ਯੋਗ ਬਣਾਉਣ ਦਾ ਮੁੱਖ ਤਰੀਕਾ ਹੈ। ਤੁਸੀਂ ਅਕਸਰ 'ਫੰਕਸ਼ਨ' ਅਤੇ 'ਟੂਲ' ਨੂੰ ਇੱਕੋ ਜਿਹਾ ਵਰਤਿਆ ਹੋਇਆ ਦੇਖੋਗੇ ਕਿਉਂਕਿ 'ਫੰਕਸ਼ਨ' (ਪੁਨ: ਵਰਤਣ ਯੋਗ ਕੋਡ ਦੇ ਬਲਾਕ) ਉਹ 'ਟੂਲ' ਹਨ ਜੋ ਏਜੰਟ ਕੰਮ ਕਰਨ ਲਈ ਵਰਤਦੇ ਹਨ। ਇੱਕ ਫੰਕਸ਼ਨ ਦੇ ਕੋਡ ਨੂੰ ਚਲਾਉਣ ਲਈ, LLM ਨੂੰ ਉਪਭੋਗਤਾ ਦੀ ਬੇਨਤੀ ਨੂੰ ਫੰਕਸ਼ਨ ਦੇ ਵੇਰਵੇ ਦੇ ਨਾਲ ਤੁਲਨਾ ਕਰਨੀ ਪੈਂਦੀ ਹੈ। ਇਸ ਲਈ, ਉਪਲਬਧ ਫੰਕਸ਼ਨਾਂ ਦੇ ਵੇਰਵੇ ਵਾਲੀ ਸਕੀਮਾ LLM ਨੂੰ ਭੇਜੀ ਜਾਂਦੀ ਹੈ। LLM ਫਿਰ ਕੰਮ ਲਈ ਸਭ ਤੋਂ ਉਚਿਤ ਫੰਕਸ਼ਨ ਦੀ ਚੋਣ ਕਰਦਾ ਹੈ ਅਤੇ ਇਸਦਾ ਨਾਮ ਅਤੇ ਪੈਰਾਮੀਟਰ ਵਾਪਸ ਕਰਦਾ ਹੈ। ਚੁਣਿਆ ਗਿਆ ਫੰਕਸ਼ਨ ਚਲਾਇਆ ਜਾਂਦਾ ਹੈ, ਇਸਦਾ ਜਵਾਬ LLM ਨੂੰ ਵਾਪਸ ਭੇਜਿਆ ਜਾਂਦਾ ਹੈ, ਜੋ ਉਪਭੋਗਤਾ ਦੀ ਬੇਨਤੀ ਦਾ ਜਵਾਬ ਦੇਣ ਲਈ ਜਾਣਕਾਰੀ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ।

ਡਿਵੈਲਪਰਾਂ ਲਈ ਏਜੰਟਾਂ ਲਈ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਲਾਗੂ ਕਰਨ ਲਈ, ਤੁਹਾਨੂੰ ਲੋੜ ਹੋਵੇਗੀ:

1. ਇੱਕ LLM ਮਾਡਲ ਜੋ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ
2. ਫੰਕਸ਼ਨ ਵੇਰਵੇ ਵਾਲੀ ਸਕੀਮਾ
3. ਹਰ ਫੰਕਸ਼ਨ ਲਈ ਕੋਡ ਜੋ ਵੇਰਵੇ ਵਿੱਚ ਦਿੱਤਾ ਗਿਆ ਹੈ

ਆਓ ਸਾਨ ਫਰਾਂਸਿਸਕੋ ਵਿੱਚ ਮੌਜੂਦਾ ਸਮਾਂ ਪ੍ਰਾਪਤ ਕਰਨ ਦੇ ਉਦਾਹਰਨ ਨਾਲ ਇਸ ਨੂੰ ਸਮਝਾਈਏ:

1. **ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦਾ ਸਮਰਥਨ ਕਰਨ ਵਾਲੇ LLM ਨੂੰ ਸ਼ੁਰੂ ਕਰੋ:**

    ਸਾਰੇ ਮਾਡਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦਾ ਸਮਰਥਨ ਨਹੀਂ ਕਰਦੇ, ਇਸ ਲਈ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ ਤੁਸੀਂ ਜੋ LLM ਵਰਤ ਰਹੇ ਹੋ ਉਹ ਕਰਦਾ ਹੈ। <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ। ਅਸੀਂ Azure OpenAI ਕਲਾਇੰਟ ਸ਼ੁਰੂ ਕਰਕੇ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹਾਂ।

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **ਫੰਕਸ਼ਨ ਸਕੀਮਾ ਬਣਾਓ:**

    ਅਗਲੇ ਕਦਮ ਵਿੱਚ, ਅਸੀਂ JSON ਸਕੀਮਾ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਾਂਗੇ ਜਿਸ ਵਿੱਚ ਫੰਕਸ਼ਨ ਦਾ ਨਾਮ, ਫੰਕਸ਼ਨ ਕੀ ਕਰਦਾ ਹੈ ਇਸਦਾ ਵੇਰਵਾ, ਅਤੇ ਫੰਕਸ਼ਨ ਪੈਰਾਮੀਟਰਾਂ ਦੇ ਨਾਮ ਅਤੇ ਵੇਰਵੇ ਸ਼ਾਮਲ ਹਨ। 

    ```python
    # Function description for the model to read
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **ਕੰਮ ਕਰਨ ਲਈ ਲੋੜੀਂਦਾ ਫੰਕਸ਼ਨ ਕੋਡ:**

    ਹੁਣ LLM ਨੇ ਚੁਣਿਆ ਹੈ ਕਿ ਕਿਹੜਾ ਫੰਕਸ਼ਨ ਚਲਾਇਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਕੰਮ ਕਰਨ ਲਈ ਲੋੜੀਂਦਾ ਕੋਡ ਲਾਗੂ ਅਤੇ ਚਲਾਇਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। 

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Handle function calls
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Second API call: Get the final response from the model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਜ਼ਿਆਦਾਤਰ, ਜੇਕਰ ਸਾਰੇ ਨਹੀਂ, ਏਜੰਟ ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਦਾ ਕੇਂਦਰ ਹੈ, ਹਾਲਾਂਕਿ ਇਸਨੂੰ ਸ਼ੁਰੂ ਤੋਂ ਲਾਗੂ ਕਰਨਾ ਕਈ ਵਾਰ ਚੁਣੌਤੀਪੂਰਨ ਹੋ ਸਕਦਾ ਹੈ। 

ਜਿਵੇਂ ਅਸੀਂ [Lesson 2](../../../02-explore-agentic-frameworks) ਵਿੱਚ ਸਿੱਖਿਆ, ਏਜੰਟਿਕ ਫਰੇਮਵਰਕ ਸਾਨੂੰ ਟੂਲ ਵਰਤੋਂ ਨੂੰ ਲਾਗੂ ਕਰਨ ਲਈ ਪਹਿਲਾਂ ਤੋਂ ਬਣੇ ਬਿਲਡਿੰਗ ਬਲਾਕ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ।

## ਏਜੰਟਿਕ ਫਰੇਮਵਰਕਾਂ ਨਾਲ ਟੂਲ ਵਰਤੋਂ ਦੇ ਉਦਾਹਰਨ

ਹੇਠਾਂ ਕੁਝ ਉਦਾਹਰਨ ਦਿੱਤੇ ਗਏ ਹਨ ਕਿ ਤੁਸੀਂ ਵੱਖ-ਵੱਖ ਏਜੰਟਿਕ ਫਰੇਮਵਰਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਨੂੰ ਕਿਵੇਂ ਲਾਗੂ ਕਰ ਸਕਦੇ ਹੋ:

### ਸੈਮੈਂਟਿਕ ਕਰਨਲ

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">ਸੈਮੈਂਟਿਕ ਕਰਨਲ</a> .NET, Python, ਅਤੇ Java ਡਿਵੈਲਪਰਾਂ ਲਈ ਇੱਕ ਖੁੱਲ੍ਹਾ-ਸਰੋਤ AI ਫਰੇਮਵਰਕ ਹੈ ਜੋ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ (LLMs) ਨਾਲ ਕੰਮ ਕਰਦੇ ਹਨ। 

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> ਇੱਕ ਨਵਾਂ ਏਜੰਟਿਕ ਫਰੇਮਵਰਕ ਹੈ ਜੋ ਡਿਵੈਲਪਰਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਤਰੀਕੇ ਨਾਲ ਉੱਚ-ਗੁਣਵੱਤਾ ਵਾਲੇ ਅਤੇ ਵਿਆਪਕ AI ਏਜੰਟਾਂ ਨੂੰ ਬਣਾਉਣ, ਡਿਪਲੌਇ ਕਰਨ, ਅਤੇ ਸਕੇਲ ਕਰਨ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ। 

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ਟੂਲ ਵਰਤੋਂ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਭਰੋਸੇਯੋਗ AI ਏਜੰਟਾਂ ਬਣਾਉਣ ਲਈ ਵਿਸ਼ੇਸ਼ ਵਿਚਾਰ ਕੀ ਹਨ?

SQL ਨੂੰ LLMs ਦੁਆਰਾ ਗਤੀਸ਼ੀਲ ਤਰੀਕੇ ਨਾਲ ਜਨਰੇਟ ਕਰਨ ਨਾਲ ਜੁੜੀ ਇੱਕ ਆਮ ਚਿੰਤਾ ਸੁਰੱਖਿਆ ਹੈ, ਖਾਸ ਕਰਕੇ SQL ਇੰਜੈਕਸ਼ਨ ਜਾਂ ਮਾਲੀਸ਼ੀਅਸ ਕਾਰਵਾਈਆਂ ਦਾ ਖਤਰਾ। 

## ਵਾਧੂ ਸਰੋਤ

-

Azure AI ਏਜੰਟਸ ਸੇਵਾ ਵਰਕਸ਼ਾਪ  
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">ਕੋਂਟੋਸੋ ਕ੍ਰੀਏਟਿਵ ਰਾਈਟਰ ਮਲਟੀ-ਏਜੰਟ ਵਰਕਸ਼ਾਪ</a>  
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">ਸੈਮੈਂਟਿਕ ਕਰਨਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਟਿਊਟੋਰਿਅਲ</a>  
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">ਸੈਮੈਂਟਿਕ ਕਰਨਲ ਕੋਡ ਇੰਟਰਪ੍ਰੀਟਰ</a>  
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">ਆਟੋਜਨ ਟੂਲਜ਼</a>  

## ਪਿਛਲਾ ਪਾਠ  

[ਏਜੰਟਿਕ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨਜ਼ ਨੂੰ ਸਮਝਣਾ](../03-agentic-design-patterns/README.md)  

## ਅਗਲਾ ਪਾਠ  

[ਏਜੰਟਿਕ RAG](../05-agentic-rag/README.md)  

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਣਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਪ੍ਰਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।