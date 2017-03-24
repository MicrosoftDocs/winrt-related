---
Description: Specifies a category of extensions that the app can host.
Search.Product: eADQiWindows 10XVcnh
title: uap3:Name
ms.assetid: bb879ff2-1f08-4bff-8b3c-0c7198c9f6da
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# uap3:Name


Specifies a category of extensions that the app can host.

## Element hierarchy


[**&lt;Package&gt;**](element-package.md)

          [**&lt;Applications&gt;**](element-applications.md)

                    [**&lt;Application&gt;**](element-application.md)

                              [**&lt;Extensions&gt;**](element-1-extensions.md)

                                        [**&lt;uap3:Extension&gt;**](element-uap3-extension-manual.md)

                                                  [**&lt;uap3:AppExtensionHost&gt;**](element-uap3-appextensionhost-manual.md)

                                                            **&lt;uap3:Name&gt;**

## Syntax


```
<uap3:Name>
    A string between 2 and 39 characters in length that consists of alphanumeric, period 
    (except for the first character), and dash characters only.
</uap3:Name>
```

## Attributes and Elements


**Attributes**

None.

**Child Elements**

None.

**Parent Elements**

| Parent Element                                                        | Description                                   |
|-----------------------------------------------------------------------|-----------------------------------------------|
| [**uap3:AppExtensionHost**](element-uap3-appextensionhost-manual.md) | Declares an extensibility point for the app.. |

 

## Examples


The following example indicates that the app can host the Office spell check and browser extensions.

```XML
<Package ...
         xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
         IgnorableNamespaces="... uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap3:Extension Category="windows.appExtensionHost">  
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


|               |                                                            |
|---------------|------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/uap/windows10/3 |

 

 

 



