---
description: Specifies a category of extensions that the app can host.
Search.Product: eADQiWindows 10XVcnh
title: uap3:Name
ms.assetid: bb879ff2-1f08-4bff-8b3c-0c7198c9f6da
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap3:Name

Specifies a category of extensions that the app can host.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap3:Extension\>](element-uap3-extension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap3:AppExtensionHost\>](element-uap3-appextensionhost-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap3:Name\>**

## Syntax

```xml
<uap3:Name>
    A string with a value between 2 and 255 characters in length that consists of alphanumeric characters, periods 
    (except for the first character), and dashes only.
</uap3:Name>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent Element | Description |
|-|-|
| [uap3:AppExtensionHost](element-uap3-appextensionhost-manual.md) | Declares an extensibility point for the app. |

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

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
