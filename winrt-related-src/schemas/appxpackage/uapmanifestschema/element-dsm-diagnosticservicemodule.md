---
title: dsm:DiagnosticServiceModule
description: Specifies a diagnostic service module file within the package that should be accessible to diagnostic tools.
keywords: windows 10, uwp, schema, manifest, extension, diagnostic service module, DAC, WER
ms.date: 07/01/2026
ms.topic: reference
no-loc: [dsm:DiagnosticServiceModule]
---

# dsm:DiagnosticServiceModule

Specifies a diagnostic service module file within the package that should be accessible to diagnostic tools.

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
  File = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **File** | The path to the diagnostic service module file, relative to the package install directory. The file must exist within the package. Path traversals that resolve outside the package install directory are rejected. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [dsm:DiagnosticServiceModules](element-dsm-diagnosticservicemodules.md) | Contains one or more diagnostic service module file declarations. |

## Remarks

During package deployment, the system grants `FILE_GENERIC_READ | FILE_GENERIC_EXECUTE` permissions to `BUILTIN\Administrators` on the file specified by the **File** attribute. This enables administrative diagnostic tools (such as Windows Error Reporting) to load the DLL from within the protected `WindowsApps` folder.

The **File** attribute specifies a path relative to the package install root. It may include subdirectory components (for example, `MyApp\mscordaccore.dll`). The resolved canonical path must remain within the package install directory; any path traversal (such as `..`) that would escape the package root causes the registration to fail with `E_INVALIDARG`.

If the file does not exist at the specified path when the package is deployed, registration fails with `HRESULT_FROM_WIN32(ERROR_FILE_NOT_FOUND)`.

### Security considerations

Only files within the MSIX package boundary can be specified. The Deployment Extension Handler validates that the canonicalized path starts with the package install directory, preventing arbitrary file ACL modifications.

The permissions granted are scoped to `BUILTIN\Administrators` with read and execute access only. This does not grant write access and does not affect non-administrator users.

## Examples

### Basic usage with a single DAC file

```xml
<dsm:Extension Category="windows.diagnosticServiceModule">
  <dsm:DiagnosticServiceModules>
    <dsm:DiagnosticServiceModule File="path\from\package\root\file_to_include.dll" />
  </dsm:DiagnosticServiceModules>
</dsm:Extension>
```

### Multiple diagnostic modules in a subdirectory

```xml
<dsm:Extension Category="windows.diagnosticServiceModule">
  <dsm:DiagnosticServiceModules>
    <dsm:DiagnosticServiceModule File="SubFolder\file_to_include.dll" />
    <dsm:DiagnosticServiceModule File="SubFolder\another_file.ext" />
  </dsm:DiagnosticServiceModules>
</dsm:Extension>
```

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/diagnosticservicemodule` |
| **Minimum OS Version** | Windows 10 version 21H2 (Build 22000) |
