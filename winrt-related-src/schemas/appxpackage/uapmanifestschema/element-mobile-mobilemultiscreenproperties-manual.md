---
Description: Declares an app extensibility point of type windows.MobileMultiScreenProperties.
Search.Product: eADQiWindows 10XVcnh
title: mobile:MobileMultiScreenProperties (Windows 10)
ms.assetid: 86ea3e53-23e4-4c7a-9490-2944dbcca460
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# mobile:MobileMultiScreenProperties (Windows 10)


Declares an app extensibility point of type **windows.MobileMultiScreenProperties**.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-mobile-extension-manual.md">&lt;mobile:Extension&gt;</a></dt>
<dd><b>&lt;mobile:MobileMultiScreenProperties&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax


```
<mobile:Extension RestrictToInternalScreen = A boolean value ("true" or "false")
</mobile:Extension>
```

## Attributes and Elements


**Attributes**

| Attribute                    | Description                                                                                                                                                                             | Data type | Required | Default value |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------|---------------|
| **RestrictToInternalScreen** | Determines whether to restrict the app's display output to the mobile device's integral screen. Setting this to true prevents the app's display from being sent to an external display. | Boolean   | Yes      | True          |

 

**Child Elements**

None.

**Parent Elements**

| Parent Element                                              | Description                                  |
|-------------------------------------------------------------|----------------------------------------------|
| [**mobile:Extension**](element-mobile-extension-manual.md) | Declares an extensibility point for the app. |

 

## Requirements


|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/mobile/windows10 |

 

 

 



