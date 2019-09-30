---
Description: Contains opaque XML that represents custom, extension-specific information that is simply stored and not read by the operating system.
Search.Product: eADQiWindows 10XVcnh
title: uap3:Properties
ms.assetid: fbc52f03-8a01-4abe-b8d1-6aa8b02eb958
author: mcleanbyron
ms.author: mcleans
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap3:Properties


Contains opaque XML that represents custom, extension-specific information that is simply stored and not read by the operating system. The information is only read by the host app.

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
<dd>
<dl>
<dt><a href="element-uap3-appextension-manual.md">&lt;uap3:AppExtension&gt;</a></dt>
<dd><b>&lt;uap3:Properties&gt;</b></dd>
</dl>
</dd>
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


```
<uap3:Properties>
  <!-- Child elements -->
  xsd:any*
</uap3:Properties>

```
### Key  
`*` optional (zero or more)

## Attributes and Elements


**Attributes**

None.

**Child Elements**

| Child Element | Description                                                                                                                                                               |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| custom        | Custom extension-specific information in the form of opaque XML that is simply stored and not read by the operating system. The information is only read by the host app. |

 

**Parent Elements**

| Parent Element                                                | Description                                                           |
|---------------------------------------------------------------|-----------------------------------------------------------------------|
| [**uap3:AppExtension**](element-uap3-appextension-manual.md) | Declares an app extensibility point of type **windows.appExtension**. |

 

## Examples


The following example indicates that the app hosts or consumes the low-performance browser extension

```XML
<Package ...
         xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
         IgnorableNamespaces="... uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap3:Extension Category="windows.appExtension">  
                    <uap3:AppExtension Name="com.microsoft.browser.ext"
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


|               |                                                            |
|---------------|------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/uap/windows10/3 |

 

 

 
