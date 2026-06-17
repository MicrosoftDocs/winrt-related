---
title: uap5:Host
description: Represents a valid HTTP or HTTPS host name with a wildcard that the app wants to register as able to handle.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap5:Extension, uap5:AppUriHandler, uap5:Host]
keywords: windows 10, uwp, schema, manifest, desktop, extension
---

# uap5:Host

Represents a valid HTTP or HTTPS host name with a wildcard that the app wants to register as able to handle.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:Extension>`](element-uap5-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap5:AppUriHandler>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap5:Host>`**

## Syntax

```xml
<uap5:Host
  Name = 'A required string between 1 and 255 characters in length.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | A wildcard with a domain name of the web site associated with the app. | A string between 1 and 255 characters in length. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap3:AppUriHandler](element-uap3-appurihandler.md) | Declares an app extensibility point of type *windows.appUriHandler*. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |

## Remarks

<!-- Author content goes here -->

## Examples

In this example, `*.microsoft.com` can be handled as: `learn.microsoft.com`, `developer.microsoft.com`, `foo.microsoft.com`, etc.

```xml
<Package ...
    xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
    xmlns:uap5="http://schemas.microsoft.com/appx/manifest/uap/windows10/5"  
    IgnorableNamespaces="... uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap3:Extension
                    Category="windows.appUriHandler">  
                    <uap3:AppUriHandler>  
                        <uap5:Host
                            Name="*.microsoft.com" />  
                    </uap3:AppUriHandler>  
                </uap3:ExtensionCategory>  
            </Extensions>
        </Application>
    </Applications>
</Package>
```
