---
ms.assetid: 485ad5c0-8ff3-4519-a388-bc40d960987d
title: com:Verb (in ExeServer/Class)
description: The verb to be registered for an application (in ExeServer/Class).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:Verb (in ExeServer/Class)

The verb to be registered for an application.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComServer\>](element-com-comserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ExeServer\>](element-com-exeserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Class\>](element-com-exeserver-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Verbs\>](element-com-exe-verbs.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:Verb\>**

## Syntax

```xml
<com:Verb
    Id = 'An integer with a value between -6 and 1000.'
    DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.'
    AppendMenuFlag = 'An integer with a value between 0 and 2431.'
    OleVerbFlag = 'An integer with a value between 0 and 3.' >
</com:Verb>
```

## Key

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The Id number of the verb. Verbs are numbered consecutively. | An integer value in the range of -6 to 1000. | Yes |  |
| **DisplayName** | Describes how the verb is appended by [AppendMenu](/windows/win32/api/winuser/nf-winuser-appendmenua). | A string between 1 and 256 characters in length. This string is localizable. | Yes |
| AppendMenuFlag | Indicates how the verb should appear in the menu. | An integer value in the range of 0 to 2431. | Yes |  |
| **OleVerbFlag** | Describes the attributes of a verb. Use either 0 or a value from the [OLEVERBATTRIB](/windows/win32/api/oleidl/ne-oleidl-oleverbattrib) enumeration. | An integer value in the range of 0 to 3. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com:Verbs](element-com-exe-verbs.md) | Specifies the verbs to be registered for an application. |

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
