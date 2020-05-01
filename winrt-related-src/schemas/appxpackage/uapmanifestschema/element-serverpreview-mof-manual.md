---
Description: Specifies the Managed Object Format (MOF) files to use to install or uninstall the Windows Management Instrumentation (WMI) provider.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:Mof
ms.assetid: 891a395f-d1b8-4d18-a05d-73701e5ed4dd


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:Mof


Specifies the Managed Object Format (MOF) files to use to install or uninstall the Windows Management Instrumentation (WMI) provider.

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
<dt><a href="element-serverpreview-wmiproviders-manual.md">&lt;serverpreview:WmiProviders&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-wmiprovider-manual.md">&lt;serverpreview:WmiProvider&gt;</a></dt>
<dd><b>&lt;serverpreview:Mof&gt;</b></dd>
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
<serverpreview:Mof InstallMof    = A string between 1 and 256 characters in 
                                   length that must end with ".mof" and cannot
                                   contain these characters: <, >, :, ", |, ?, 
                                   or *. 
                   UninstallMof? = A string between 1 and 256 characters in 
                                   length that must end with ".mof" and cannot 
                                   contain these characters: <, >, :, ", |, ?, 
                                   or *. >
</serverpreview:Mof>
```

**Key**

          ? optional (zero or one)

## Attributes and Elements


**Attributes**

| Attribute        | Description                                                                                                                                                     | Data type                                                                                                                                     | Required | Default value |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------|
| **InstallMof**   | The file name of the MOF file to use to install the WMI provider. This file name must be unique to the package, and the MOF file must be part of the package.   | A string between 1 and 256 characters in length that must end with ".mof" and cannot contain these characters: &lt;, &gt;, :, ", |, ?, or \*. | Yes      |               |
| **UninstallMof** | The file name of the MOF file to use to uninstall the WMI provider. This file name must be unique to the package, and the MOF file must be part of the package. | A string between 1 and 256 characters in length that must end with ".mof" and cannot contain these characters: &lt;, &gt;, :, ", |, ?, or \*. | No       |               |

 

**Child Elements**

None.

**Parent Elements**

| Parent Element                                                                | Description                                                                            |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**serverpreview:WmiProvider**](element-serverpreview-wmiprovider-manual.md) | Identifies a WMI provider to install, update, or uninstall out-of-band on Nano Server. |

 

## Examples


```XML
<Package ...
         xmlns:serverpreview=http://schemas.microsoft.com/appx/manifest/serverpreview/windows10"  
         IgnorableNamespaces="... serverpreview">
    <Applications>
        <Application>
            <Extensions>
                <serverpreview:Extension Category="windows.wmiProviders">  
                    <serverpreview:WmiProviders>  
                        <serverpreview:WmiProvider 
                                Name="ProviderName"
                                Namespace="root\standardcimv2"
                                HostingSpecification="networkServiceHost"
                                HostingGroup="ProviderGroup">  
                            <serverpreview:Mof 
                                    InstallMof="Install.mof"
                                    UninstallMof="Uninstall.mof"/>  
                        </serverpreview:WmiProvider>  
                        <serverpreview:WmiProvider  
                                Name="ProviderName2"  
                                Namespace="root\standardcimv2"
                                HostingSpecification="decoupled:Com"
                                DecoupledProviderExecutable="serviceExec.exe">  
                            <serverpreview:Mof  
                                    InstallMof="Install2.mof"  
                                    UninstallMof="Uninstall2.mof"/>  
                        </serverpreview:WmiProvider>  
                    </serverpreview:WmiProviders>  
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

 

 

 



