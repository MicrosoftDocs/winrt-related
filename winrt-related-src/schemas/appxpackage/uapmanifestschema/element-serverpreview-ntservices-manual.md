---
Description: Declares an app extensibility point of type windows.ntServices.
MS-HAID: UapManifestSchema.element\_serverpreview\_ntservices\_manual
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:NTServices
ms.assetid: d405e0f2-5dd2-4dd7-bfc6-0cf85842ce74
author: laurenhughes
ms.author: lahugh
keywords: windows 10
---

# serverpreview:NTServices


Declares an app extensibility point of type **windows.ntServices**. This element identifies one or more NT Services to install, update, or uninstall on Nano Server.

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
<dd><b>&lt;serverpreview:NTServices&gt;</b></dd>
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
<serverpreview:NTServices>
  <!-- Child elements -->
  serverpreview:NTService{1,100}
</serverpreview:NTServices>
```

**Key**

          {} specific range of occurrences

## Attributes and Elements


**Attributes**

None.

**Child Elements**

| Child Element                                                             | Description                                                               |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [**serverpreview:NTService**](element-serverpreview-ntservice-manual.md) | Identifies an NT Service to install, update, or uninstall on Nano Server. |

 

**Parent Elements**

| Parent Element                                                            | Description                                  |
|---------------------------------------------------------------------------|----------------------------------------------|
| [**serverpreview:Extension**](element-serverpreview-extension-manual.md) | Declares an extensibility point for the app. |

 

## Examples


```XML
12345678901234567890123456789012345678901234567890123456789012345678901234567890
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
                                Executable="serviceExec.exe"
                                StartupType="auto"  
                                DisplayName="service Display Name"  
                                StartErrorAction="ignoreError" 
                                StartAccount="localService"    
                                Description="service1 description"   
                                StartParameters="arg1 arg2"
                                FailureRecoveryAction="restartService"> 
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

 

 

 



