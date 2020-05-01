---
Description: Specifies the set of additional services on which the service that corresponds to the parent serverpreview:NTService element depends.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:ServiceDependencies
ms.assetid: 354cd254-29db-42e7-98f4-db235e8aba0a


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:ServiceDependencies


Specifies the set of additional services on which the service that corresponds to the parent [serverpreview:NTService](element-serverpreview-ntservice-manual.md) element depends.

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
<dd><b>&lt;serverpreview:ServiceDependencies&gt;</b></dd>
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
<serverpreview:ServiceDependencies>
  <!-- Child elements -->
  serverpreview:ServiceDependency{1,100}
</serverpreview:ServiceDependencies>
```

**Key**

          {} specific range of occurrences

## Attributes and Elements


**Attributes**

None.

**Child Elements**

| Child Element                                                                             | Description                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**serverpreview:ServiceDependency**](element-serverpreview-servicedependency-manual.md) | Specifies an additional service on which the service that corresponds to the grandparent [serverpreview:NTService](element-serverpreview-ntservice-manual.md) element depends. |

 

**Parent Elements**

| Parent Element                                                            | Description                                                                           |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**serverpreview:NTService**](element-serverpreview-ntservice-manual.md) | Identifies an NT Service to install, update, or uninstall out-of-band on Nano Server. |

 

## Remarks


Service dependencies must be other services in the package.

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
                                Name="depServiceName"  
                                Executable="depServiceExec.exe"                  
                                StartupType="auto"  
                                StartAccount="networkService"  
                                DisplayName="depServiceName" >  
                        </serverpreview:NTService>             
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
                            <serverpreview:ServiceDependencies>
                                <serverpreview:ServiceDependency 
                                        Name ="depServiceName"/>  
                            </serverpreview:ServiceDependencies>   
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

 

 

 



