---
Description: Allows for a packaged app to declare API redirections.
title: uap7:ImportRedirectionTable


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 10/03/2018
---

# uap7:ImportRedirectionTable

Allows for a packaged app to declare API redirections. API redirection allows apps to consume legacy binaries that link against unsupported APIs (e.g., CreateFile) and transparently replace them with supported APIs (e.g., CreateFileFromApp) at module load time.

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
<dt><a href="element-uap7-properties.md">&lt;uap7:Properties&gt;</a></dt>
<dd><b>&lt;uap7:ImportRedirectionTable&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<uap7:ImportRedirectionTable>

  A DLL file.

</uap7:ImportRedirectionTable>
```

## Attributes and Elements
### Attributes
None 

### Child Elements
None

## Remarks
The DLL file is passed to CreateProcess to influence how the loader resolves imports.

## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
