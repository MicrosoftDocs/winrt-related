---
title: uap3:AppExtensionHost
description: Declares an app extensibility point of type windows.appExtensionHost.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap3:Extension, uap3:AppExtensionHost]
---

# uap3:AppExtensionHost

Declares an app extensibility point of type *windows.appExtensionHost*. This element indicates which categories of extensions the app can host.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap3:Extension>`](element-uap3-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap3:AppExtensionHost>`**  

## Syntax

```xml
<uap3:AppExtensionHost>

  <!-- Child elements -->
  uap3:Name{1,unbounded}

</uap3:AppExtensionHost>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap3:Name](element-uap3-name.md) | Specifies a category of extensions that the app can host. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap3:Extension](element-uap3-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |

## Remarks

For a packaged app to see/enumerate appextensions it must meet at least one of the following criteria:

- Run as MediumIL (or higher)
- Run in an AppContainer and declare a matching appextensionhost
- Run in an AppContainer and have the packageQuery capability

This check is called by [AppExtensionCatalog.Open](/uwp/api/windows.applicationmodel.appextensions.appextensioncatalog.open) and [AppExtensionCatalog::RequestRemovePackageAsync](/uwp/api/windows.applicationmodel.appextensions).

## Examples

The following example indicates that the app can host the Office spell check and browser extensions.

```xml
<Package
    xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
    IgnorableNamespaces="... uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap3:Extension
                    Category="windows.appExtensionHost">  
                    <uap3:AppExtensionHost>  
                        <uap3:Name>com.microsoft.office.spellcheck.ext</uap3:Name>
                        <uap3:Name>com.microsoft.office.browser.ext</uap3:Name>  
                    </uap3:AppExtensionHost>  
                </uap3:Extension>
            </Extensions>
        </Application>
    </Applications>
</Package>
```
