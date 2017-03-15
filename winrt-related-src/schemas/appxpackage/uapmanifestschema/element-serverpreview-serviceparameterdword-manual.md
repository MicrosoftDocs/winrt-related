---
Description: Specifies the value of a parameter for the service that has a data type of REG\_DWORD.
MS-HAID: UapManifestSchema.element\_serverpreview\_serviceparameterdword\_manual
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:ServiceParameterDword
ms.assetid: 96e0ef7e-d90d-4d55-893d-cb3ed146e403
author: laurenhughes
ms.author: lahugh
keywords: windows 10
---

# serverpreview:ServiceParameterDword


Specifies the value of a parameter for the service that has a data type of **REG\_DWORD**. This parameter corresponds to a registry value that is created under the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\*ServiceName*\\Parameters** key or specified subkey.

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
<dd><b>&lt;serverpreview:ServiceParameterDword&gt;</b></dd>
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
<serverpreview:ServiceParameterDword Name    = A string between 1 and 16,383 
                                               characters in length with a non-
                                               whitespace character at its 
                                               beginning and end.
                                     Value   = An unsigned integer.
                                     Subkey? = A string between 1 and 255  
                                               characters in length that cannot  
                                               start or endwith a period or  
                                               contain these characters: <, >,  
                                               :, ", /, \, |, ?, or *. >
</serverpreview:ServiceParameterDword>
```

**Key**

          ? optional (zero or one)

## Attributes and Elements


**Attributes**

| Attribute  | Description                                                                                                                                                                                                                                                                                                                                      | Data type                                                                                                                                                 | Required | Default value |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------|
| **Name**   | The name of the parameter to set.                                                                                                                                                                                                                                                                                                                | A string between 1 and 16,383 characters in length with a non-whitespace character at its beginning and end.                                              | Yes      |               |
| **Value**  | The value to use for the parameter.                                                                                                                                                                                                                                                                                                              | An unsigned integer.                                                                                                                                      | Yes      |               |
| **Subkey** | The subkey under the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\*ServiceName*\\Parameters** key under which the registry value should be located. If you do not specify this attribute, the registry value is located directly under **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\*ServiceName*\\Parameters**. | A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: &lt;, &gt;, :, ", /, \\, |, ?, or \*. | No       |               |

 

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
                                <serverpreview:ServiceParameterDword  
                                        Name="paramName4" 
                                        Value="1"/>
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

 

 

 



