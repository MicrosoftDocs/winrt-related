---
title: uap3:Properties
description: Contains opaque XML that represents custom, extension-specific information that is simply stored and not read by the operating system.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap3:Extension, uap3:AppExtension, uap3:Properties]
keywords: windows 10, uwp, schema, package manifest
---

# uap3:Properties

Contains opaque XML that represents custom, extension-specific information that is simply stored and not read by the operating system. The information is only read by the host app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap3:Extension>`](element-uap3-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap3:AppExtension>`](element-uap3-appextension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap3:Properties>`**

## Syntax

```xml
<uap3:Properties>
  xsd:any
</uap3:Properties>
```

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| **custom** | Custom extension-specific information in the form of opaque XML that is simply stored and not read by the operating system. The information is only read by the host app. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap3:AppExtension](element-uap3-appextension.md) | Declares an app extensibility point of type *windows.appExtension*. This element indicates which categories of extensions the app intends to consume and/or host. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |

## Remarks

<!-- Author content goes here -->

## Examples

The following example indicates that the app hosts or consumes a high-performance browser extension

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
