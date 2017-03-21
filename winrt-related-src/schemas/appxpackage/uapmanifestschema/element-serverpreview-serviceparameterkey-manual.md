---
Description: Specifies a parameter for the service. This parameter corresponds to a registry subkey that is created under the HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\ServiceName\\Parameters key.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:ServiceParameterKey
ms.assetid: 0a9cf40b-d5da-415c-8c4b-3b879bb6e969
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# serverpreview:ServiceParameterKey


Specifies a parameter for the service. This parameter corresponds to a registry subkey that is created under the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\*ServiceName*\\Parameters** key.

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
<dt><a href="element-serverpreview-ntservices-manual.md">&lt;serverpreview:NTServices&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-ntservice-manual.md">&lt;serverpreview:NTService&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-serviceparameters-manual.md">&lt;serverpreview:ServiceParameters&gt;</a></dt>
<dd><b>&lt;serverpreview:ServiceParameterKey&gt;</b></dd>
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
</dd>
</dl>
</dd>
</dl>

## Syntax


```
<serverpreview:ServiceParameterKey Subkey = A string between 1 and 255  
                                            characters in length that cannot  
                                            start or endwith a period or  
                                            contain these characters: <, >,  
                                            :, ", /, \, |, ?, or *. >
</serverpreview:ServiceParameterKey>
```

## Attributes and Elements


**Attributes**

| Attribute  | Description                                                                                                                  | Data type                                                                                                                                                 | Required | Default value |
|------------|------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------|
| **Subkey** | The subkey to create under the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\*ServiceName*\\Parameters** key. | A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: &lt;, &gt;, :, ", /, \\, |, ?, or \*. | Yes      |               |

 

**Child Elements**

None.

**Parent Elements**

| Parent Element                                                                            | Description                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**serverpreview:ServiceParameters**](element-serverpreview-serviceparameters-manual.md) | Specifies a set of parameters to configure for the service. These parameters correspond to registry values that are created under the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\*ServiceName*\\Parameters** key. |

 

## Examples


```XML
<Package ...
         xmlns:serverpreview=http://schemas.microsoft.com/appx/manifest/serverpreview/windows10"  
         IgnorableNamespaces="... serverpreview">
    <Applications>
       <Application Id="TestService">
            <uap:VisualElements AppListEntry="none" 
                                DisplayName="TestService" 
                                Square150x150Logo="logo.png" 
                                Square44x44Logo="logo.png" 
                                Description="TestService" 
                                BackgroundColor="#777777"/>
            <Extensions>
                <serverpreview:Extension Category="windows.ntServices">  
                    <serverpreview:NTServices>  
                        <serverpreview:NTService  
                                Name="serviceName"  
                                Executable="depServiceExec.exe"                  
                                StartupType="auto"  
                                StartAccount="networkService"  
                                DisplayName="depServiceName" >  
                            <serverpreview:ServiceParameters>  
                                <serverpreview:ServiceParameterKey 
                                        Subkey="key1\key2"/>  
                            </serverpreview:ServiceParameters>                      
                        </serverpreview:NTService> 
                    </serverpreview:NTServices>  
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

 

 

 



