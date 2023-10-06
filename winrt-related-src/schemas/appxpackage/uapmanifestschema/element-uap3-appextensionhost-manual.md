---
description: Declares an app extensibility point of type windows.appExtensionHost.
Search.Product: eADQiWindows 10XVcnh
title: uap3:AppExtensionHost
ms.assetid: 632f4bda-7822-4d90-a3a1-688ed4b7cf24
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap3:AppExtensionHost

Declares an app extensibility point of type *windows.appExtensionHost*. This element indicates which categories of extensions the app can host.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap3:Extension\>](element-uap3-extension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap3:AppExtensionHost\>**

## Syntax

```xml
<uap3:AppExtensionHost>

  <!-- Child elements -->
  uap3:Name

</uap3:AppExtensionHost>
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [uap3:Name](element-uap3-name-manual.md) | Specifies a category of extensions that the app can host. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap3:Extension](element-uap3-extension-manual.md) | Declares an extensibility point for the app. |

## Remarks

for a packaged app to see/enumerate appextensions it must meet at least one of the following criteria:

- Run as MediumIL (or higher)
- Run in an AppContainer and declare a matching appextensionhost
- Run in an AppContainer and have the packageQuery capability

This check is called by [AppExtensionCatalog.Open](/uwp/api/windows.applicationmodel.appextensions.appextensioncatalog.open) and [AppExtensionCatalog::RequestRemovePackageAsync](/uwp/api/windows.applicationmodel.appextensions.

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

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
