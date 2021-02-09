---
description: Specifies a set of parameters to configure for the service.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:ServiceParameters
ms.assetid: 321cca00-b107-4109-9187-c712f2621aae


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:ServiceParameters


Specifies a set of parameters to configure for the service. These parameters correspond to registry values that are created under the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\*ServiceName*\\Parameters** key.

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
<dd><b>&lt;serverpreview:ServiceParameters&gt;</b></dd>
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
<serverpreview:ServiceParameters>
  <!-- Child elements -->
  ( serverpreview:ServiceParamerterDword |
    serverpreview:ServiceParameterString |
    serverpreview:ServiceParametersKey ){1,100}
</serverpreview:ServiceParameters>
```

**Key**

          {} specific range of occurrences

## Attributes and Elements


**Attributes**

None.

**Child Elements**

| Child Element                                                                                       | Description                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**serverpreview:ServiceParameterDword**](element-serverpreview-serviceparameterdword-manual.md)   | Specifies the value of a parameter for the service that has a data type of **REG\_DWORD**. This parameter corresponds to a registry value that is created under the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\*ServiceName*\\Parameters** key or specified subkey. |
| [**serverpreview:ServiceParameterString**](element-serverpreview-serviceparameterstring-manual.md) | Specifies the value of a parameter for the service that has a data type of **REG\_SZ**. This parameter corresponds to a registry value that is created under the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\*ServiceName*\\Parameters** key or specified subkey.    |
| [**serverpreview:ServiceParameterKey**](element-serverpreview-serviceparameterkey-manual.md)       | Specifies a parameter for the service. This parameter corresponds to a registry subkey that is created under the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\*ServiceName*\\Parameters** key.                                                                        |

 

**Parent Elements**

| Parent Element                                                            | Description                                                                           |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**serverpreview:NTService**](element-serverpreview-ntservice-manual.md) | Identifies an NT Service to install, update, or uninstall out-of-band on Nano Server. |

 

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
                                <serverpreview:ServiceParameterString 
                                        Name="paramName2" 
                                        Value="paramVal"/>
                                <serverpreview:ServiceParameterString 
                                        Name="paramName3" 
                                        Value="paramVal"/>    
                                <serverpreview:ServiceParameterDword  
                                        Name="paramName4" 
                                        Value="1"/>
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
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/serverpreview/windows10` |

 

 

 



