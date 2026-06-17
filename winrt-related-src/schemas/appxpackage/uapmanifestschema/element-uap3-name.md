---
title: uap3:Name
description: Specifies a category of extensions that the app can host.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap3:Extension, uap3:AppExtensionHost, uap3:Name]
keywords: windows 10, uwp, schema, package manifest
---

# uap3:Name

Specifies a category of extensions that the app can host.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap3:Extension>`](element-uap3-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap3:AppExtensionHost>`](element-uap3-appextensionhost.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap3:Name>`**

## Syntax

```xml
<uap3:Name>
    A string with a value between 2 and 255 characters in length that consists of alphanumeric characters, periods
    (except for the first character), and dashes only.
</uap3:Name>
```

## Attributes

None.

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap3:AppExtensionHost](element-uap3-appextensionhost.md) | Declares an app extensibility point of type *windows.appExtensionHost*. This element indicates which categories of extensions the app can host. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |

## Remarks

<!-- Author content goes here -->

## Examples

The following example indicates that the app can host the Office spell check and browser extensions.

```xml
<Package ...
    xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
    IgnorableNamespaces="uap3">
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
