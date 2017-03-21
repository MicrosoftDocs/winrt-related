---
Description: Represents a valid HTTP or HTTPS host name that the app wants to register as able to handle.
Search.Product: eADQiWindows 10XVcnh
title: uap3:Host
ms.assetid: 7635ea1b-a5f8-4347-a553-8cabb62d7102
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# uap3:Host


Represents a valid HTTP or HTTPS host name that the app wants to register as able to handle.

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
<dt><a href="element-uap3-appurihandler-manual.md">&lt;uap3:AppUriHandler&gt;</a></dt>
<dd><b>&lt;uap3:Host&gt;</b></dd>
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
<uap3:Host Name = >
</uap3:Host>
```

**Key**

          {} specific range of occurrences

## Attributes and Elements


**Attributes**

| Attribute | Description                                                              | Data type                                       | Required | Default value |
|-----------|--------------------------------------------------------------------------|-------------------------------------------------|----------|---------------|
| **Name**  | The fully-qualified domain name of the web site associated with the app. | A string between 1 and 255 characters in length | Yes      |               |

 

**Child Elements**

None.

**Parent Elements**

| Parent Element                                                  | Description                                                            |
|-----------------------------------------------------------------|------------------------------------------------------------------------|
| [**uap3:AppUriHandler**](element-uap3-appurihandler-manual.md) | Declares an app extensibility point of type **windows.appUriHandler**. |

 

## Examples


```XML
<Package ...
         xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
         IgnorableNamespaces="... uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap3:Extension Category="windows.appUriHandler">  
                    <uap3:AppUriHandler>  
                        <uap3:Host Name="www.app-uri-handler.com" />  
                        <uap3:Host Name="appUriHandler.com" />  
                    </uap3:AppUriHandler>  
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

 

 

 



