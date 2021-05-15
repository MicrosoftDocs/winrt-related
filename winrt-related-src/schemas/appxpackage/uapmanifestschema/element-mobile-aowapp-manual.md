---
description: Declares an app extensibility point of type windows.aowApp.
Search.Product: eADQiWindows 10XVcnh
title: mobile:AowApp (Windows 10)
ms.assetid: 5a716d59-0796-4584-890f-98f26b0654ce


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# mobile:AowApp (Windows 10)


Declares an app extensibility point of type **windows.aowApp**.

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
<dd><b>&lt;mobile:AowApp&gt;</b></dd>
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
<mobile:Extension
  <!-- Child elements -->
  ( mobile:PayloadName
  &amp; mobile:PayloadVersion
  )

</mobile:Extension>
```

**Key**

          & interleave connector (may occur in any order)

## Attributes and Elements


**Attributes**

None.

**Child Elements**

| Child Element             | Description                                                                                                                       |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **mobile:PayloadName**    | An element containing a string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. |
| **mobile:PayloadVersion** | An element containing a string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. |

 

**Parent Elements**

| Parent Element                                              | Description                                  |
|-------------------------------------------------------------|----------------------------------------------|
| [**mobile:Extension**](element-mobile-extension-manual.md) | Declares an extensibility point for the app. |

 

## Requirements


|               | Value                                                         |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/mobile/windows10` |

 

 

 



