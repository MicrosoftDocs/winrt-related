---
description: Identifies a performance counter to add to the server-specific app extensions.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:PerformanceProvider
ms.assetid: 6601d242-568d-4260-8aae-1d0b2965aaae


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:PerformanceProvider


Identifies a performance counter to add to the server-specific app extensions.

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
<dd>
<dl>
<dt><a href="element-serverpreview-performanceproviders-manual.md">&lt;serverpreview:PerformanceProviders&gt;</a></dt>
<dd><b>&lt;serverpreview:PerformanceProvider&gt;</b></dd>
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
<serverpreview:PerformanceProvider Id           = GUID in the form 
                                                  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.  
                                   ManifestFile = A string between 1 and 256 characters in 
                                                  length that  must end with ".xml" and 
                                                  cannot contain these characters: <, >, 
                                                  :, ", |, ?, or *.
                                   ResourceFile = A string between 1 and 256 characters in 
                                                  length that  must end with ".exe"  or 
                                                  ".dll" and cannot contain these 
                                                  characters: <, >, :, ", |, ?, or *. >
</serverpreview:PerformanceProvider>
```

## Attributes and Elements


**Attributes**

| Attribute        | Description                                                            | Data type                                                                                                                                               | Required | Default value |
|------------------|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------|
| **Id**           | The unique identifier of the performance counter provider.             | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.                                                                                                | Yes      |               |
| **ManifestFile** | The name of the manifest file for the performance counter.             | A string between 1 and 256 characters in length that must end with ".xml" and cannot contain these characters: &lt;, &gt;, :, ", \|, ?, or \*.           | Yes      |               |
| **ResourceFile** | The name of the application resource file for the performance counter. | A string between 1 and 256 characters in length that must end with ".exe" or ".dll" and cannot contain these characters: &lt;, &gt;, :, ", \|, ?, or \*. | Yes      |               |

 

**Child Elements**

None.

**Parent Elements**

| Parent Element                                                                                 | Description                                                                   |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [**severpreview:PerformanceProviders**](element-serverpreview-performanceproviders-manual.md) | Declares an app extensibility point of type **windows.performanceProviders**. |

 

## Remarks


The performance counter extension is only available only on the Windows Server platform. This extension is ignored on other platforms.

The performance counter extension allows only V2 providers.

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


|               | Value                                                              |
|---------------|--------------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/serverpreview/windows10` |

 

 

 



