---
title: uap3:Host
description: Represents a valid HTTP or HTTPS host name that the app wants to register as able to handle.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap3:Extension, uap3:AppUriHandler, uap3:Host]
keywords: windows 10, uwp, schema, package manifest
---

# uap3:Host

Represents a valid HTTP or HTTPS host name that the app wants to register as able to handle.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap3:Extension>`](element-uap3-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap3:AppUriHandler>`](element-uap3-appurihandler.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap3:Host>`**

## Syntax

```xml
<uap3:Host
  Name = 'A required string between 1 and 255 characters in length.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The fully-qualified domain name of the web site associated with the app. | A string between 1 and 255 characters in length. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap3:AppUriHandler](element-uap3-appurihandler.md) | Declares an app extensibility point of type *windows.appUriHandler*. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |

## Remarks

<!-- Author content goes here -->

## Examples

```xml
<Package
    xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
    IgnorableNamespaces="... uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap3:Extension
                    Category="windows.appUriHandler">  
                    <uap3:AppUriHandler>  
                        <uap3:Host
                            Name="www.app-uri-handler.com" />  
                        <uap3:Host
                            Name="appUriHandler.com" />  
                    </uap3:AppUriHandler>  
                </uap3:Extension>  
            </Extensions>
        </Application>
    </Applications>
</Package>
```
