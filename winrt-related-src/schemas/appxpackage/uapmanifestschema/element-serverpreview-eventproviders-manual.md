---
description: Declares an app extensibility point of type windows.eventProviders.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:EventProviders
ms.assetid: cfc8b89e-1eef-4fee-adeb-70039588c5a9


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:EventProviders


Declares an app extensibility point of type **windows.eventProviders**. This element identifies one or more event tracing extensions to add to the server-specific app extensions.

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
<dt><a href="element-serverpreview-extension-manual.md">&lt;serverpreview:Extension&gt;</a></dt>
<dd><b>&lt;serverpreview:EventProviders&gt;</b></dd>
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
<serverpreview:EventProviders>
  <!-- Child elements -->
  serverpreview:EventProvider{1,100}
</serverpreview:EventProviders>
```

**Key**

          {} specific range of occurrences

## Attributes and Elements


**Attributes**

None.

**Child Elements**

| Child Element                                                                     | Description                                                                         |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**serverpreview:EventProvider**](element-serverpreview-eventprovider-manual.md) | Identifies an event tracing extension to add to the server-specific app extensions. |

 

**Parent Elements**

| Parent Element                                                            | Description                                  |
|---------------------------------------------------------------------------|----------------------------------------------|
| [**serverpreview:Extension**](element-serverpreview-extension-manual.md) | Declares an extensibility point for the app. |

 

## Examples


The following example identifies an event tracing extension to add to the server-specific app extensions.

```XML
<Package ...
         xmlns:serverpreview=http://schemas.microsoft.com/appx/manifest/serverpreview/windows10"  
         IgnorableNamespaces="... serverpreview">
    <Applications>
        <Application>
            <Extensions>
                <serverpreview:Extension Category="windows.eventProviders">  
                    <serverpreview:EventProviders>  
                        <serverpreview:EventProvider Id="66fc99f0-b9c7-40f6-90bd-5d9a86b6c02a"  
                                                     ManifestFile="EventProvider.man"  
                                                     ResourceFile="EventSample.exe" />  
                    </serverpreview:EventProviders>  
                </serverpreview:Extension>  
            </Extensions>
        </Application>
    </Applications>
</Package>
```

## Requirements


|               |                                                                    |
|---------------|--------------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/serverpreview/windows10` |

 

 

 



