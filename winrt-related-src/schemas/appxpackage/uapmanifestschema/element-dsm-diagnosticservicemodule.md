---
title: dsm:DiagnosticServiceModule
description: Specifies a package diagnostic service module file for access by diagnostic tools.
keywords: windows 10, windows 11, schema, manifest, extension, diagnostic service module, DAC, WER
ms.date: 09/18/2026
ms.topic: reference
no-loc: [dsm:DiagnosticServiceModule]
---

# dsm:DiagnosticServiceModule

Specifies a package diagnostic service module file for access by diagnostic tools.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<dsm:Extension>`](element-dsm-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<dsm:DiagnosticServiceModules>`](element-dsm-diagnosticservicemodules.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<dsm:DiagnosticServiceModule>`**  

## Syntax

```xml
<dsm:DiagnosticServiceModule
  File = 'A package-relative path.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **File** | The package-relative path to the diagnostic service module file. | A string containing a package-relative path. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [dsm:DiagnosticServiceModules](element-dsm-diagnosticservicemodules.md) | Contains one or more diagnostic service module file declarations. |

## Remarks

During package deployment, the system grants
`FILE_GENERIC_READ | FILE_GENERIC_EXECUTE` permissions to `BUILTIN\Administrators` on the file
specified by the **File** attribute. This enables administrative diagnostic tools (such as
Windows Error Reporting) to load the DLL from within the protected `WindowsApps` folder.

### Security considerations

The permissions granted are scoped to `BUILTIN\Administrators` with read and execute access only.
This doesn't grant write access and doesn't affect non-administrator users.

## Examples

### Basic usage with a single diagnostic module

```xml
<dsm:Extension Category="windows.diagnosticServiceModule">
  <dsm:DiagnosticServiceModules>
    <dsm:DiagnosticServiceModule File="path\from\package\root\file_to_include.dll" />
  </dsm:DiagnosticServiceModules>
</dsm:Extension>
```

### Multiple diagnostic modules

```xml
<dsm:Extension Category="windows.diagnosticServiceModule">
  <dsm:DiagnosticServiceModules>
    <dsm:DiagnosticServiceModule File="foo\dump.dll" />
    <dsm:DiagnosticServiceModule File="bar\diagnostic_debug_aid.dll" />
  </dsm:DiagnosticServiceModules>
</dsm:Extension>
```

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/diagnosticservicemodule` |
| **Minimum Windows App SDK Version** | 2.5.1 |
