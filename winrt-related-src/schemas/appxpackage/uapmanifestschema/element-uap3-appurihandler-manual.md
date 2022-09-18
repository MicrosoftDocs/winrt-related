---
description: Declares an app extensibility point of type windows.appUriHandler.
Search.Product: eADQiWindows 10XVcnh
title: uap3:AppUriHandler
ms.assetid: 3ec18f36-df44-46c1-ae8f-721c77e715d5
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 07/23/2021
---

# uap3:AppUriHandler

Declares an app extensibility point of type *windows.appUriHandler*.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap3-extension-manual.md">&lt;uap3:Extension&gt;</a></dt>
<dd><b>&lt;uap3:AppUriHandler&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<uap3:AppUriHandler
    desktop2:Parameters = 'An optional string format of parameters (for example, `/L %1`).'
    uap7:Name = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child elements -->
  uap3:Host{0,1000}
  uap5:Host{0,1000}

</uap3:AppUriHandler>
```

### Key

`{}`  specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **desktop2:Parameters** | Specifies how to pass the URI handler into the app. `%1` is a token that specifies the full path. | A string format of parameters (for example, `/L %1`). | No |  |
| **uap7:Name** | A friendly name for the app URI handler. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [uap3:Host](element-uap3-host-manual.md) | Represents a valid HTTP or HTTPS host name that the app wants to register as able to handle. |
| [uap5:Host](element-uap5-host.md) | Represents a valid HTTP or HTTPS host name with a wildcard that the app wants to register as able to handle. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap3:Extension](element-uap3-extension-manual.md) | Declares an extensibility point for the app.. |

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

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
