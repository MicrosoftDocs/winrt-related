---
description: Contains opaque XML that represents custom, extension-specific information that is simply stored and not read by the operating system.
Search.Product: eADQiWindows 10XVcnh
title: uap3:Properties
ms.assetid: fbc52f03-8a01-4abe-b8d1-6aa8b02eb958
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap3:Properties

Contains opaque XML that represents custom, extension-specific information that is simply stored and not read by the operating system. The information is only read by the host app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap3:Extension\>](element-uap3-extension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap3:AppExtension\>](element-uap3-appextension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap3:Properties\>**

## Syntax

```xml
<uap3:Properties>
  xsd:any
</uap3:Properties>
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| **custom** | Custom extension-specific information in the form of opaque XML that is simply stored and not read by the operating system. The information is only read by the host app. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap3:AppExtension](element-uap3-appextension-manual.md) | Declares an app extensibility point of type *windows.appExtension*. |

## Examples

The following example indicates that the app hosts or consumes the low-performance browser extension

```xml
<Package ...
    xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
    IgnorableNamespaces="uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap3:Extension
                    Category="windows.appExtension">  
                    <uap3:AppExtension
                        Name="com.microsoft.browser.ext"
                        Id="Extension.High.Performance"
                        PublicFolder="public\highperf"
                        DisplayName="High Performance Extension">  
                        <uap3:Properties>  
                            <!-- The content of this element is custom. -->
                            <animals>Chickens</animals>  
                            <animals>  
                                <young>Kittens</young>  
                            </animals>  
                          </uap3:Properties>  
                      </uap3:AppExtension>  
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
