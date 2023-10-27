---
title: uap6:LocalExperiencePack
description: This extension provides a means to deliver translated app resources (in Package/Applications).
ms.date: 04/10/2018
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap6:LocalExperiencePack

This extension provides a means to deliver translated app resources.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap6:Extension\>](element-uap6-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap6:LocalExperiencePack\>**

## Syntax

```xml
<uap6:LocalExperiencePack
  Language = 'A string that represents a language and locale, containing four characters separated by a dash (for example, "en-us" or "fr-fr").' />
```

### Key

`?`   optional (zero or one)

## Attrbutes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Language** | The language and locale identifier. For example, `en-us` represents English language used in the United States. | A string that represents a language and locale, containing four characters separated by a dash (for example, `en-us` or `fr-fr`). | No |  |

### Child elements

None

### Parent elements

| Parent element | Description |
|-|-|
| [uap6:Extension](element-uap6-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/6` |
| Minimum OS Version | Windows 10 version 1803 (Build 17134) |
