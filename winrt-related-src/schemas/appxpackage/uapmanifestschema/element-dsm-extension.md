---
title: dsm:Extension
description: Declares an extensibility point for a diagnostic service module extension.
keywords: windows 10, windows 11, schema, manifest, extension, diagnostic service module, DAC
ms.date: 09/18/2026
ms.topic: reference
no-loc: [Package, Extensions, dsm:Extension]
---

# dsm:Extension

Specifies a list of diagnostic service module files (for example, .NET Data Access Component DLLs)
for access by diagnostic tools (for example, Windows Error Reporting).

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<dsm:Extension>`**  

## Syntax

```xml
<dsm:Extension
  Category = "windows.diagnosticServiceModule" >

  <!-- Child Elements -->
  dsm:DiagnosticServiceModules

</dsm:Extension>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Category** | The category of the extension. | Must be the value *windows.diagnosticServiceModule*. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [dsm:DiagnosticServiceModules](element-dsm-diagnosticservicemodules.md) | Contains one or more diagnostic service module file declarations. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions (in Application)](element-f-application-extensions.md) | Defines one or more extensibility points for the application. |
| [Extensions (in Package)](element-extensions.md) | Defines one or more extensibility points for the package. |

## Remarks

The `windows.diagnosticServiceModule` extension specifies diagnostic service module files within
the MSIX package that need to be accessible to diagnostic tools running outside the package
container. During package deployment, the system grants
`FILE_GENERIC_READ | FILE_GENERIC_EXECUTE` permissions to `BUILTIN\Administrators` on the
specified files, enabling diagnostic tools like Windows Error Reporting (WER) to load them.

A common use case is specifying the .NET Data Access Component (DAC) DLL (`mscordaccore.dll`) for
self-contained .NET applications deployed via MSIX. Without this extension, the DAC files inside
the `WindowsApps` folder are inaccessible to WER, resulting in crash dumps that lack managed
debugging information.

## Examples

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10"
  xmlns:dsm="http://schemas.microsoft.com/appx/manifest/diagnosticservicemodule"
  IgnorableNamespaces="dsm">

  <!-- ... -->

  <Applications>
    <Application Id="App" Executable="MyApp.exe" EntryPoint="Windows.FullTrustApplication">
      <Extensions>
        <dsm:Extension Category="windows.diagnosticServiceModule">
          <dsm:DiagnosticServiceModules>
            <dsm:DiagnosticServiceModule File="path\from\package\root\file_to_include.dll" />
            <dsm:DiagnosticServiceModule File="relative\path\to\another_file.ext" />
          </dsm:DiagnosticServiceModules>
        </dsm:Extension>
      </Extensions>
    </Application>
  </Applications>

</Package>
```

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/diagnosticservicemodule` |
| **Minimum Windows App SDK Version** | 2.5.1 |
