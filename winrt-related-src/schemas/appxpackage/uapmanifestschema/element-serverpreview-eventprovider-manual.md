---
Description: Identifies an event tracing extension to add to the server-specific app extensions.
MS-HAID: UapManifestSchema.element\_serverpreview\_eventprovider\_manual
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:EventProvider
ms.assetid: 7992570a-0250-49e8-9f9a-5196028e262e
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# serverpreview:EventProvider


Identifies an event tracing extension to add to the server-specific app extensions.

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
<dt><a href="element-serverpreview-eventproviders-manual.md">&lt;serverpreview:EventProviders&gt;</a></dt>
<dd><b>&lt;serverpreview:EventProvider&gt;</b></dd>
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
<serverpreview:EventProvider Id           = GUID in the form 
                                            xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.  
                             ManifestFile = A string between 1 and 256 characters in 
                                            length that  must end with ".xml" and cannot 
                                            contain these characters: <, >, :, ", |, ?, or 
                                            *.
                             ResourceFile = A string between 1 and 256 characters in 
                                            length that  must end with ".exe"  or ".dll" 
                                            and cannot contain these characters: <, >, :, 
                                            ", |, ?, or *. >
</serverpreview:EventProvider>
```

## Attributes and Elements


**Attributes**

| Attribute        | Description                                                                | Data type                                                                                                                                               | Required | Default value |
|------------------|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------|
| **Id**           | The unique identifier of the event tracing provider.                       | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.                                                                                                | Yes      |               |
| **ManifestFile** | The name of the manifest file for the event tracing extension.             | A string between 1 and 256 characters in length that must end with ".man" and cannot contain these characters: &lt;, &gt;, :, ", |, ?, or \*.           | Yes      |               |
| **ResourceFile** | The name of the application resource file for the event tracing extension. | A string between 1 and 256 characters in length that must end with ".exe" or ".dll" and cannot contain these characters: &lt;, &gt;, :, ", |, ?, or \*. | Yes      |               |

 

**Child Elements**

None.

**Parent Elements**

| Parent Element                                                                     | Description                                                             |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**severpreview:EventProviders**](element-serverpreview-eventproviders-manual.md) | Declares an app extensibility point of type **windows.eventProviders**. |

 

## Remarks


The event tracing extension is only available only on the Windows Server platform. This extension is ignored on other platforms.

The event tracing extension allows only manifest-based providers.

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
| **Namespace** | http://schemas.microsoft.com/appx/manifest/serverpreview/windows10 |

 

 

 



