<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b4c2650691b24b20e0c912d01a466a2",
  "translation_date": "2025-08-21T13:40:31+00:00",
  "source_file": "README.md",
  "language_code": "hu"
}
-->
# AI Ügynökök Kezdőknek - Egy Tanfolyam

![Generative AI For Beginners](../../translated_images/repo-thumbnail.083b24afed61b6dd27a7fc53798bebe9edf688a41031163a1fca9f61c64d63ec.hu.png)

## 11 lecke, amelyek mindent megtanítanak, amit tudnod kell az AI ügynökök építésének elkezdéséhez

[![GitHub license](https://img.shields.io/github/license/microsoft/ai-agents-for-beginners.svg)](https://github.com/microsoft/ai-agents-for-beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)  
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)  
[![GitHub issues](https://img.shields.io/github/issues/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/issues/?WT.mc_id=academic-105485-koreyst)  
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/ai-agents-for-beginners.svg)](https://GitHub.com/microsoft/ai-agents-for-beginners/pulls/?WT.mc_id=academic-105485-koreyst)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

### 🌐 Többnyelvű támogatás

#### GitHub Action által támogatott (Automatikus és mindig naprakész)

[Francia](../fr/README.md) | [Spanyol](../es/README.md) | [Német](../de/README.md) | [Orosz](../ru/README.md) | [Arab](../ar/README.md) | [Perzsa (Fárszi)](../fa/README.md) | [Urdu](../ur/README.md) | [Kínai (Egyszerűsített)](../zh/README.md) | [Kínai (Hagyományos, Makaó)](../mo/README.md) | [Kínai (Hagyományos, Hongkong)](../hk/README.md) | [Kínai (Hagyományos, Tajvan)](../tw/README.md) | [Japán](../ja/README.md) | [Koreai](../ko/README.md) | [Hindi](../hi/README.md) | [Bengáli](../bn/README.md) | [Marathi](../mr/README.md) | [Nepáli](../ne/README.md) | [Pandzsábi (Gurmukhi)](../pa/README.md) | [Portugál (Portugália)](../pt/README.md) | [Portugál (Brazília)](../br/README.md) | [Olasz](../it/README.md) | [Lengyel](../pl/README.md) | [Török](../tr/README.md) | [Görög](../el/README.md) | [Thai](../th/README.md) | [Svéd](../sv/README.md) | [Dán](../da/README.md) | [Norvég](../no/README.md) | [Finn](../fi/README.md) | [Holland](../nl/README.md) | [Héber](../he/README.md) | [Vietnámi](../vi/README.md) | [Indonéz](../id/README.md) | [Maláj](../ms/README.md) | [Tagalog (Filippínó)](../tl/README.md) | [Szuahéli](../sw/README.md) | [Magyar](./README.md) | [Cseh](../cs/README.md) | [Szlovák](../sk/README.md) | [Román](../ro/README.md) | [Bolgár](../bg/README.md) | [Szerb (Cirill)](../sr/README.md) | [Horvát](../hr/README.md) | [Szlovén](../sl/README.md) | [Ukrán](../uk/README.md) | [Burmai (Mianmar)](../my/README.md)

**Ha további fordításokat szeretnél, a támogatott nyelvek listáját [itt találod](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/ai-agents-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/ai-agents-for-beginners/watchers/?WT.mc_id=academic-105485-koreyst)  
[![GitHub forks](https://img.shields.io/github/forks/microsoft/ai-agents-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/ai-agents-for-beginners/network/?WT.mc_id=academic-105485-koreyst)  
[![GitHub stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/ai-agents-for-beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://discord.gg/kzRShWzttr)

## 🌱 Kezdés

Ez a tanfolyam 11 leckét tartalmaz, amelyek az AI ügynökök építésének alapjait fedik le. Minden lecke egyedi témát dolgoz fel, így ott kezdheted, ahol szeretnéd!

Ez a tanfolyam többnyelvű támogatást nyújt. Nézd meg az [elérhető nyelveket itt](../..).  

Ha ez az első alkalom, hogy Generatív AI modellekkel dolgozol, nézd meg a [Generative AI For Beginners](https://aka.ms/genai-beginners) tanfolyamunkat, amely 21 leckét tartalmaz a GenAI-val való munkáról.

Ne felejtsd el [csillagozni (🌟) ezt a repót](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) és [forkolni ezt a repót](https://github.com/microsoft/ai-agents-for-beginners/fork), hogy futtathasd a kódot.

### Mire lesz szükséged

A tanfolyam minden leckéje tartalmaz kódpéldákat, amelyek a code_samples mappában találhatók. [Forkold ezt a repót](https://github.com/microsoft/ai-agents-for-beginners/fork), hogy létrehozd a saját másolatodat.  

A gyakorlatok kódpéldái az Azure AI Foundry-t és a GitHub Model Catalogs-t használják a nyelvi modellekkel való interakcióhoz:

- [Github Modellek](https://aka.ms/ai-agents-beginners/github-models) - Ingyenes / Korlátozott
- [Azure AI Foundry](https://aka.ms/ai-agents-beginners/ai-foundry) - Azure fiók szükséges

Ez a tanfolyam a következő AI ügynök keretrendszereket és szolgáltatásokat használja a Microsofttól:

- [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service)  
- [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel)  
- [AutoGen](https://aka.ms/ai-agents/autogen)  

További információért a tanfolyam kódjának futtatásáról, látogasd meg a [Tanfolyam Beállítás](./00-course-setup/README.md) oldalt.

## 🙏 Szeretnél segíteni?

Van javaslatod, vagy találtál helyesírási vagy kódhibát? [Nyiss egy hibajegyet](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) vagy [Hozz létre egy pull requestet](https://github.com/microsoft/ai-agents-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)

Ha elakadsz, vagy bármilyen kérdésed van az AI ügynökök építésével kapcsolatban, csatlakozz az [Azure AI Foundry Community Discord](https://discord.gg/kzRShWzttr) közösséghez.  

Ha termék-visszajelzésed van, vagy hibákat tapasztalsz az építés során, látogasd meg az [Azure AI Foundry Fejlesztői Fórumot](https://aka.ms/azureaifoundry/forum).

## 📂 Minden lecke tartalmazza

- Egy írott leckét a README-ben és egy rövid videót  
- Python kódpéldákat, amelyek támogatják az Azure AI Foundry-t és a Github Modelleket (Ingyenes)  
- Linkeket további tanulási forrásokhoz  

## 🗃️ Leckék

| **Lecke**                                | **Szöveg & Kód**                                  | **Videó**                                                  | **További Tanulás**                                                                 |
|------------------------------------------|--------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------------------------------|
| Bevezetés az AI ügynökökbe és felhasználási esetek | [Link](./01-intro-to-ai-agents/README.md)        | [Videó](https://youtu.be/3zgm60bXmQk?si=z8QygFvYQv-9WtO1)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ügynöki keretrendszerek felfedezése   | [Link](./02-explore-agentic-frameworks/README.md)| [Videó](https://youtu.be/ODwF-EZo_O8?si=Vawth4hzVaHv-u0H)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ügynöki tervezési minták megértése    | [Link](./03-agentic-design-patterns/README.md)   | [Videó](https://youtu.be/m9lM8qqoOEA?si=BIzHwzstTPL8o9GF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Eszközhasználati tervezési minta         | [Link](./04-tool-use/README.md)                  | [Videó](https://youtu.be/vieRiPRx-gI?si=2z6O2Xu2cu_Jz46N)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Ügynöki RAG                              | [Link](./05-agentic-rag/README.md)               | [Videó](https://youtu.be/WcjAARvdL7I?si=gKPWsQpKiIlDH9A3)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Megbízható AI ügynökök építése           | [Link](./06-building-trustworthy-agents/README.md)| [Videó](https://youtu.be/iZKkMEGBCUQ?si=jZjpiMnGFOE9L8OK ) | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Tervezési minta: Tervezés                | [Link](./07-planning-design/README.md)           | [Videó](https://youtu.be/kPfJ2BrBCMY?si=6SC_iv_E5-mzucnC)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Többügynökös tervezési minta             | [Link](./08-multi-agent/README.md)               | [Videó](https://youtu.be/V6HpE9hZEx0?si=rMgDhEu7wXo2uo6g)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| Metakogníció tervezési minta             | [Link](./09-metacognition/README.md)             | [Videó](https://youtu.be/His9R6gw6Ec?si=8gck6vvdSNCt6OcF)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ügynökök a gyakorlatban               | [Link](./10-ai-agents-production/README.md)      | [Videó](https://youtu.be/l4TP6IyJxmQ?si=31dnhexRo6yLRJDl)  | [Link](https://aka.ms/ai-agents-beginners/collection?WT.mc_id=academic-105485-koreyst) |
| AI ügynökök MCP-vel                      | [Link](./11-mcp/README.md)                       |                                                            | [Link](https://aka.ms/mcp-for-beginners)                                               |

## 🎒 Egyéb tanfolyamok

Csapatunk más tanfolyamokat is készít! Nézd meg:
- [**ÚJ** Model Context Protocol (MCP) Kezdőknek](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Generatív MI Kezdőknek .NET használatával](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [Generatív MI Kezdőknek](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Generatív MI Kezdőknek Java használatával](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
- [Gépi Tanulás Kezdőknek](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [Adattudomány Kezdőknek](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [MI Kezdőknek](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [Kiberbiztonság Kezdőknek](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Webfejlesztés Kezdőknek](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [IoT Kezdőknek](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [XR Fejlesztés Kezdőknek](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [GitHub Copilot Mesterfokon az MI Alapú Páros Programozáshoz](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [GitHub Copilot Mesterfokon C#/.NET Fejlesztőknek](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [Válaszd Ki a Saját Copilot Kalandodat](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

## 🌟 Közösségi Köszönetnyilvánítás

Köszönet [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) számára, hogy fontos kódrészletekkel járult hozzá az Agentic RAG bemutatásához. 

## Hozzájárulás

Ez a projekt szívesen fogad hozzájárulásokat és javaslatokat. A legtöbb hozzájárulás esetén szükséges, hogy elfogadj egy 
Hozzájárulói Licencszerződést (CLA), amelyben kijelented, hogy jogod van a hozzájárulásod felhasználásának engedélyezésére, és ezt meg is teszed. Részletekért látogass el ide: 
<https://cla.opensource.microsoft.com>.

Amikor egy pull requestet nyújtasz be, egy CLA bot automatikusan meghatározza, hogy szükséges-e CLA-t biztosítanod, és ennek megfelelően megjelöli a PR-t (pl. státuszellenőrzés, megjegyzés). Egyszerűen kövesd a bot által adott utasításokat. Ezt csak egyszer kell megtenned az összes olyan repó esetében, amely a CLA-t használja.

Ez a projekt elfogadta a [Microsoft Nyílt Forráskódú Magatartási Kódexét](https://opensource.microsoft.com/codeofconduct/).
További információért lásd a [Magatartási Kódex GYIK](https://opensource.microsoft.com/codeofconduct/faq/) oldalt, vagy lépj kapcsolatba a [opencode@microsoft.com](mailto:opencode@microsoft.com) címen bármilyen további kérdéssel vagy megjegyzéssel.

## Védjegyek

Ez a projekt tartalmazhat védjegyeket vagy logókat projektekhez, termékekhez vagy szolgáltatásokhoz. A Microsoft védjegyek vagy logók engedélyezett használata a 
[Microsoft Védjegy- és Márkaútmutatójának](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) megfelelően történhet. 
A Microsoft védjegyek vagy logók módosított verziókban történő használata nem okozhat zavart vagy nem sugallhatja a Microsoft támogatását. 
Harmadik felek védjegyeinek vagy logóinak használata az adott harmadik felek szabályzatainak hatálya alá tartozik.

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.