---
title: uap5:Host
description: Represents a valid HTTP or HTTPS host name with a wildcard that the app wants to register as able to handle.
ms.date: 10/10/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:Host

Represents a valid HTTP or HTTPS host name with a wildcard that the app wants to register as able to handle.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap3:Extension\>](element-uap3-extension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap3:AppUriHandler\>](element-uap3-appurihandler-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap5:Host\>**

## Syntax

```xml
<uap5:Host
    Name = 'A wildcard ("*") and a period (".") character followed by an alphanumeric domain name string value.' />
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name**  | A wildcard with a domain name of the web site associated with the app. | A wildcard (`*`) and a period (`.`) character followed by an alphanumeric domain name string value. | Yes  |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap3:AppUriHandler](element-uap3-appurihandler-manual.md) | Declares an app extensibility point of type *windows.appUriHandler*. |

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

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| Minimum OS Version | Windows 10 version 1709 (Build 16299) |
