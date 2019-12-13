---
Description: Declares an app extensibility point of type windows.performanceProviders.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:PerformanceProviders
ms.assetid: 63366b04-0493-4bea-918b-7bab027d5e29


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:PerformanceProviders


Declares an app extensibility point of type **windows.performanceProviders**. This element identifies one or more performance counters to add to the server-specific app extensions.

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
<dd><b>&lt;serverpreview:PerformanceProviders&gt;</b></dd>
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
<serverpreview:PerformanceProviders>
  <!-- Child elements -->
  serverpreview:PerformanceProvider{1,100}
</serverpreview:PerformanceProviders>
```

**Key**

          {} specific range of occurrences

## Attributes and Elements


**Attributes**

None.

**Child Elements**

| Child Element                                                                                 | Description                                                                    |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**serverpreview:PerformanceProvider**](element-serverpreview-performanceprovider-manual.md) | Identifies a performance counter to add to the server-specific app extensions. |

 

**Parent Elements**

| Parent Element                                                            | Description                                  |
|---------------------------------------------------------------------------|----------------------------------------------|
| [**serverpreview:Extension**](element-serverpreview-extension-manual.md) | Declares an extensibility point for the app. |

 

## Examples


The following example identifies a performance counter to add to the server-specific app extensions.

```XML
<Package ...
         xmlns:serverpreview=http://schemas.microsoft.com/appx/manifest/serverpreview/windows10"  
         IgnorableNamespaces="... serverpreview">
    <Applications>
        <Application>
            <Extensions>
                <serverpreview:Extension Category="windows.performanceProviders">  
                    <serverpreview:PerformanceProviders>  
                        <serverpreview:PerformanceProvider Id="19b99d4e-deef-4de5-9fe8-5d53a01f79e0"
                                                           ManifestFile="Counters.xml"  
                                                           ResourceFile="PerfSample.exe" />  
                    </serverpreview:PerformanceProviders>  
                </serverpreview:Extension>  
            </Extensions>
        </Application>
    </Applications>
</Package>
```

## Requirements


|               |                                                                    |
|---------------|--------------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/serverpreview/windows10 |

 

 

 



