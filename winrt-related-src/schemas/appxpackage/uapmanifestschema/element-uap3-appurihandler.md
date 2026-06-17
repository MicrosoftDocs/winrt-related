---
title: uap3:AppUriHandler
description: Declares an app extensibility point of type windows.appUriHandler.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap3:Extension, uap3:AppUriHandler]
---

# uap3:AppUriHandler

Declares an app extensibility point of type *windows.appUriHandler*.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap3:Extension>`](element-uap3-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap3:AppUriHandler>`**  

## Syntax

```xml
<uap3:AppUriHandler
  desktop2:Parameters = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  uap7:Name = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child elements -->
  uap3:Host{0,1000}
  uap3:Host{0,1000}

</uap3:AppUriHandler>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **desktop2:Parameters** | Specifies how to pass the URI handler into the app. `%1` is a token that specifies the full path. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap7:Name** | A friendly name for the app URI handler. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap3:Host](element-uap3-host.md) | Represents a valid HTTP or HTTPS host name that the app wants to register as able to handle. |
| [uap5:Host](element-uap5-host.md) | Represents a valid HTTP or HTTPS host name with a wildcard that the app wants to register as able to handle. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap3:Extension](element-uap3-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| **desktop2** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
| **uap7** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
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
