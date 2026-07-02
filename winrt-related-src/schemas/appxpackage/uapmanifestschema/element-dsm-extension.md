---
title: dsm:Extension
description: Declares an extensibility point for the diagnostic service module extension (dsm:Extension).
keywords: windows 10, uwp, schema, manifest, extension, diagnostic service module, DAC
ms.date: 07/01/2026
ms.topic: reference
no-loc: [Package, Extensions, dsm:Extension]
---

# dsm:Extension

Declares an extensibility point that registers diagnostic service module files (such as .NET Data Access Component DLLs) for access by diagnostic tools like Windows Error Reporting.

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

The `windows.diagnosticServiceModule` extension registers DLL files within the MSIX package that need to be accessible to diagnostic tools running outside the package container. During package deployment, the system grants `FILE_GENERIC_READ | FILE_GENERIC_EXECUTE` permissions to `BUILTIN\Administrators` on the specified files, enabling diagnostic tools like Windows Error Reporting (WER) to load them.

A common use case is registering the .NET Data Access Component (DAC) DLL (`mscordaccore.dll`) for self-contained .NET applications deployed via MSIX. Without this extension, the DAC files inside the WindowsApps folder are inaccessible to WER, resulting in crash dumps that lack managed debugging information.

The `dsm` namespace should be declared as ignorable in the `<Package>` element so that older OS versions that do not recognize this extension category will skip it without failing package installation.

> [!NOTE]
> This extension is processed by an undocked Deployment Extension Handler (DEH) that ships with the Windows App SDK. The DEH parses the manifest XML directly, so it works on OS versions that predate built-in knowledge of the `diagnosticservicemodule` namespace.

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
| **Minimum OS Version** | Windows 10 version 21H2 (Build 22000) |
