---
Description: Declares an app extensibility point of type windows.appExtensionHost.
Search.Product: eADQiWindows 10XVcnh
title: uap3:AppExtensionHost
ms.assetid: 632f4bda-7822-4d90-a3a1-688ed4b7cf24


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap3:AppExtensionHost


Declares an app extensibility point of type **windows.appExtensionHost**. This element indicates which categories of extensions the app can host.

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
<dd><b>&lt;uap3:AppExtensionHost&gt;</b></dd>
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
<uap3:AppExtensionHost>
  <!-- Child elements -->
  uap3:Name+
</uap3:AppExtensionHost>
```

**Key**  
    \+ one or more

## Attributes and Elements


**Attributes**

None.

**Child Elements**

| Child Element                                  | Description                                               |
|------------------------------------------------|-----------------------------------------------------------|
| [**uap3:Name**](elemennt-uap3-name-manual.md) | Specifies a category of extensions that the app can host. |

 

**Parent Elements**

| Parent Element                                          | Description                                   |
|---------------------------------------------------------|-----------------------------------------------|
| [**uap3:Extension**](element-uap3-extension-manual.md) | Declares an extensibility point for the app.. |

 

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


|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |

 

 

 
