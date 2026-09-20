---
title: dsm:DiagnosticServiceModules
description: Contains one or more diagnostic service module file declarations.
keywords: windows 10, windows 11, schema, manifest, extension, diagnostic service module, DAC
ms.date: 09/18/2026
ms.topic: reference
no-loc: [dsm:DiagnosticServiceModules]
---

# dsm:DiagnosticServiceModules

Contains one or more diagnostic service module file declarations.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<dsm:Extension>`](element-dsm-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<dsm:DiagnosticServiceModules>`**  

## Syntax

```xml
<dsm:DiagnosticServiceModules>

  <!-- Child Elements -->
  dsm:DiagnosticServiceModule{1,unbounded}

</dsm:DiagnosticServiceModules>
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [dsm:DiagnosticServiceModule](element-dsm-diagnosticservicemodule.md) | Specifies a diagnostic service module file. |

### Parent elements

| Parent element | Description |
|-|-|
| [dsm:Extension](element-dsm-extension.md) | Declares the diagnostic service module extensibility point. |

## Remarks

This element must contain at least one
[dsm:DiagnosticServiceModule](element-dsm-diagnosticservicemodule.md) child element.

## Examples

```xml
<dsm:DiagnosticServiceModules>
  <dsm:DiagnosticServiceModule File="path\from\package\root\file_to_include.dll" />
  <dsm:DiagnosticServiceModule File="relative\path\to\another_file.ext" />
</dsm:DiagnosticServiceModules>
```

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/diagnosticservicemodule` |
| **Minimum Windows App SDK Version** | 2.5.1 |
