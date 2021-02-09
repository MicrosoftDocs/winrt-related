---
description: Declares an app extensibility point of type windows.wmiProviders.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:WmiProviders
ms.assetid: d24842b2-5c15-4dbb-bd57-85348819c21a


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:WmiProviders


Declares an app extensibility point of type **windows.wmiProviders**. This element identifies one or more Windows Management Instrumentation (WMI) providers to install, update, or uninstall out-of-band on Nano Server.

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
<dd><b>&lt;serverpreview:WmiProviders&gt;</b></dd>
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
<serverpreview:WmiProviders>
  <!-- Child elements -->
  serverpreview:WmiProvider{1,100}
</serverpreview:WmiProviders>
```

**Key**

          {} specific range of occurrences

## Attributes and Elements


**Attributes**

None.

**Child Elements**

| Child Element                                                                 | Description                                                                            |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**serverpreview:WmiProvider**](element-serverpreview-wmiprovider-manual.md) | Identifies a WMI provider to install, update, or uninstall out-of-band on Nano Server. |

 

**Parent Elements**

| Parent Element                                                            | Description                                  |
|---------------------------------------------------------------------------|----------------------------------------------|
| [**serverpreview:Extension**](element-serverpreview-extension-manual.md) | Declares an extensibility point for the app. |

 

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

 

 

 



