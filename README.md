[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/YFgwt0yY)
# MiniTorch Module 2

<img src="https://minitorch.github.io/minitorch.svg" width="50%">


* Docs: https://minitorch.github.io/

* Overview: https://minitorch.github.io/module2/module2/

This assignment requires the following files from the previous assignments. You can get these by running

```bash
python sync_previous_module.py previous-module-dir current-module-dir
```

The files that will be synced are:

        minitorch/operators.py minitorch/module.py minitorch/autodiff.py minitorch/scalar.py minitorch/scalar_functions.py minitorch/module.py project/run_manual.py project/run_scalar.py project/datasets.py



1. Simple 
Number of points: 50
Size of Hidden Layer: 2
Learning Rate: 0.5
Number of Epochs: 500.
Epoch 500/500. Time per epoch: 0.033s. Time left: 0.00s.
Logs:
Epoch: 0/500, loss: 0, correct: 0
Epoch: 10/500, loss: 33.367573903149264, correct: 30
Epoch: 20/500, loss: 32.972918497616476, correct: 30
Epoch: 30/500, loss: 32.25689239264538, correct: 30
Epoch: 40/500, loss: 30.806593405628025, correct: 30
Epoch: 50/500, loss: 27.935904875300732, correct: 30
Epoch: 60/500, loss: 23.097713892909304, correct: 42
Epoch: 70/500, loss: 16.644252079940994, correct: 47
Epoch: 80/500, loss: 12.610109216248159, correct: 46
Epoch: 90/500, loss: 12.485888234957034, correct: 44
Epoch: 100/500, loss: 5.2561925848565005, correct: 50
Epoch: 110/500, loss: 3.723339730447207, correct: 50
Epoch: 120/500, loss: 2.9476564723963343, correct: 50
Epoch: 130/500, loss: 2.494039221260283, correct: 50
Epoch: 140/500, loss: 2.1639353295727832, correct: 50
Epoch: 150/500, loss: 1.9242804182073237, correct: 50
Epoch: 160/500, loss: 1.743155207181834, correct: 50
Epoch: 170/500, loss: 1.6114595831013567, correct: 50
Epoch: 180/500, loss: 1.5923084106036605, correct: 50
Epoch: 190/500, loss: 1.9651448709697572, correct: 49
Epoch: 200/500, loss: 9.638837865613972, correct: 47
Epoch: 210/500, loss: 1.6105681975352375, correct: 50
Epoch: 220/500, loss: 1.3638650738281919, correct: 50
Epoch: 230/500, loss: 1.2537386807953685, correct: 50
Epoch: 240/500, loss: 1.1654040889779476, correct: 50
Epoch: 250/500, loss: 1.092045678913083, correct: 50
Epoch: 260/500, loss: 1.0302482241821722, correct: 50
Epoch: 270/500, loss: 0.9765306110029548, correct: 50
Epoch: 280/500, loss: 0.9289483448367643, correct: 50
Epoch: 290/500, loss: 0.8871690310891893, correct: 50
Epoch: 300/500, loss: 0.8496774788457294, correct: 50
Epoch: 310/500, loss: 0.8156868894531847, correct: 50
Epoch: 320/500, loss: 0.7846082139550551, correct: 50
Epoch: 330/500, loss: 0.7559884546169687, correct: 50
Epoch: 340/500, loss: 0.729472910759011, correct: 50
Epoch: 350/500, loss: 0.704779351811182, correct: 50
Epoch: 360/500, loss: 0.6816821540811089, correct: 50
Epoch: 370/500, loss: 0.6600850746232872, correct: 50
Epoch: 380/500, loss: 0.6397740783325665, correct: 50
Epoch: 390/500, loss: 0.6206047980603732, correct: 50
Epoch: 400/500, loss: 0.6024284401407279, correct: 50
Epoch: 410/500, loss: 0.5851542568711606, correct: 50
Epoch: 420/500, loss: 0.5687045808424898, correct: 50
Epoch: 430/500, loss: 0.5530123394161559, correct: 50
Epoch: 440/500, loss: 0.5380191356219847, correct: 50
Epoch: 450/500, loss: 0.5236737422727722, correct: 50
Epoch: 460/500, loss: 0.5099309086668979, correct: 50
Epoch: 470/500, loss: 0.496750406266604, correct: 50
Epoch: 480/500, loss: 0.4840962588880052, correct: 50
Epoch: 490/500, loss: 0.4719361166789052, correct: 50
Epoch: 500/500, loss: 0.46024074313094204, correct: 50




2. Diag
Number of points: 50
Size of Hidden Layer: 2
Learning Rate: 0.5
Number of Epochs: 500.
Epoch 500/500. Time per epoch: 0.034s. Time left: 0.00s.
Logs:
Epoch: 0/500, loss: 0, correct: 0
Epoch: 10/500, loss: 10.124979752642842, correct: 48
Epoch: 20/500, loss: 8.57104602537363, correct: 48
Epoch: 30/500, loss: 8.33465263304355, correct: 48
Epoch: 40/500, loss: 8.241735565824262, correct: 48
Epoch: 50/500, loss: 8.164701915253648, correct: 48
Epoch: 60/500, loss: 8.089425415914267, correct: 48
Epoch: 70/500, loss: 8.012954116355377, correct: 48
Epoch: 80/500, loss: 7.933552691762519, correct: 48
Epoch: 90/500, loss: 7.8496750115952665, correct: 48
Epoch: 100/500, loss: 7.759776936712383, correct: 48
Epoch: 110/500, loss: 7.662210763354244, correct: 48
Epoch: 120/500, loss: 7.555121954256094, correct: 48
Epoch: 130/500, loss: 7.436328843175321, correct: 48
Epoch: 140/500, loss: 7.303169306906423, correct: 48
Epoch: 150/500, loss: 7.152294874300031, correct: 48
Epoch: 160/500, loss: 6.979387142637869, correct: 48
Epoch: 170/500, loss: 6.778766719541453, correct: 48
Epoch: 180/500, loss: 6.542871105727109, correct: 48
Epoch: 190/500, loss: 6.261626735731429, correct: 48
Epoch: 200/500, loss: 5.921923931822252, correct: 48
Epoch: 210/500, loss: 5.5079530759081505, correct: 48
Epoch: 220/500, loss: 5.004472228972299, correct: 48
Epoch: 230/500, loss: 4.406871188130674, correct: 48
Epoch: 240/500, loss: 3.77325433841779, correct: 48
Epoch: 250/500, loss: 3.385359944069198, correct: 48
Epoch: 260/500, loss: 3.09530448644189, correct: 48
Epoch: 270/500, loss: 2.856605724289427, correct: 48
Epoch: 280/500, loss: 2.655627494701062, correct: 48
Epoch: 290/500, loss: 2.463466774417677, correct: 48
Epoch: 300/500, loss: 2.3251809515916078, correct: 48
Epoch: 310/500, loss: 2.168167615773354, correct: 48
Epoch: 320/500, loss: 2.0145587482970266, correct: 48
Epoch: 330/500, loss: 1.8958110984230607, correct: 48
Epoch: 340/500, loss: 1.7611689944691868, correct: 48
Epoch: 350/500, loss: 1.6585367235132296, correct: 48
Epoch: 360/500, loss: 1.5534148424379837, correct: 50
Epoch: 370/500, loss: 1.4682980583039442, correct: 50
Epoch: 380/500, loss: 1.3992287764344737, correct: 50
Epoch: 390/500, loss: 1.301443459207738, correct: 50
Epoch: 400/500, loss: 1.2430682940359465, correct: 50
Epoch: 410/500, loss: 1.175277953510287, correct: 50
Epoch: 420/500, loss: 1.1053180927272068, correct: 50
Epoch: 430/500, loss: 1.0472949761526347, correct: 50
Epoch: 440/500, loss: 1.0072253990561273, correct: 50
Epoch: 450/500, loss: 0.958011040301616, correct: 50
Epoch: 460/500, loss: 0.912155766097998, correct: 50
Epoch: 470/500, loss: 0.8704317002239649, correct: 50
Epoch: 480/500, loss: 0.8305033812746653, correct: 50
Epoch: 490/500, loss: 0.7869644929508095, correct: 50
Epoch: 500/500, loss: 0.7506231266762601, correct: 50




3. Split
Number of points: 50
Size of Hidden Layer: 2
Learning Rate: 0.5
Number of Epochs: 500.
Epoch 500/500. Time per epoch: 0.034s. Time left: 0.00s.
Logs:
Epoch: 0/500, loss: 0, correct: 0
Epoch: 10/500, loss: 34.34209663143849, correct: 28
Epoch: 20/500, loss: 33.72834519598348, correct: 32
Epoch: 30/500, loss: 33.41592256543419, correct: 33
Epoch: 40/500, loss: 32.97638986818754, correct: 33
Epoch: 50/500, loss: 32.316189574395516, correct: 34
Epoch: 60/500, loss: 31.401039139467514, correct: 37
Epoch: 70/500, loss: 30.281296527314645, correct: 38
Epoch: 80/500, loss: 28.92277987330056, correct: 38
Epoch: 90/500, loss: 27.696186404770888, correct: 38
Epoch: 100/500, loss: 27.247224521128636, correct: 37
Epoch: 110/500, loss: 26.98375549291469, correct: 37
Epoch: 120/500, loss: 26.82956141467132, correct: 37
Epoch: 130/500, loss: 26.440080817863315, correct: 37
Epoch: 140/500, loss: 24.415995951708485, correct: 38
Epoch: 150/500, loss: 23.81708557425304, correct: 38
Epoch: 160/500, loss: 23.08457816863399, correct: 38
Epoch: 170/500, loss: 21.980319860222597, correct: 38
Epoch: 180/500, loss: 31.05368647537989, correct: 34
Epoch: 190/500, loss: 18.2475040953424, correct: 39
Epoch: 200/500, loss: 15.786522447517099, correct: 42
Epoch: 210/500, loss: 16.792784811959926, correct: 44
Epoch: 220/500, loss: 14.849141065814525, correct: 44
Epoch: 230/500, loss: 14.693716784424877, correct: 44
Epoch: 240/500, loss: 11.86796415892975, correct: 48
Epoch: 250/500, loss: 32.25688898785145, correct: 37
Epoch: 260/500, loss: 11.93506239408206, correct: 48
Epoch: 270/500, loss: 9.76291673018879, correct: 48
Epoch: 280/500, loss: 15.143438991311767, correct: 43
Epoch: 290/500, loss: 12.49497757714717, correct: 45
Epoch: 300/500, loss: 11.259773492888757, correct: 47
Epoch: 310/500, loss: 11.007070341154344, correct: 45
Epoch: 320/500, loss: 10.173141612783962, correct: 47
Epoch: 330/500, loss: 9.629118069924328, correct: 47
Epoch: 340/500, loss: 9.780971869844421, correct: 47
Epoch: 350/500, loss: 9.549509757715672, correct: 47
Epoch: 360/500, loss: 9.192745637372225, correct: 47
Epoch: 370/500, loss: 9.039854888908527, correct: 47
Epoch: 380/500, loss: 8.840065450147991, correct: 47
Epoch: 390/500, loss: 8.60825462504708, correct: 47
Epoch: 400/500, loss: 8.403185460712077, correct: 47
Epoch: 410/500, loss: 8.059471080694742, correct: 47
Epoch: 420/500, loss: 7.602243770692228, correct: 47
Epoch: 430/500, loss: 6.862192141478691, correct: 48
Epoch: 440/500, loss: 5.485178614566815, correct: 48
Epoch: 450/500, loss: 4.6199148139872, correct: 48
Epoch: 460/500, loss: 3.9360909780107414, correct: 48
Epoch: 470/500, loss: 4.081208891843723, correct: 48
Epoch: 480/500, loss: 4.2220808645054095, correct: 48
Epoch: 490/500, loss: 4.0164062434212315, correct: 48
Epoch: 500/500, loss: 3.924811162815275, correct: 48



4. Xor
Number of points: 50
Size of Hidden Layer: 2
Learning Rate: 0.5
Number of Epochs: 500.
Epoch 500/500. Time per epoch: 0.034s. Time left: 0.00s.
Logs:
Epoch: 0/500, loss: 0, correct: 0
Epoch: 10/500, loss: 34.563038489152255, correct: 27
Epoch: 20/500, loss: 34.492730961601374, correct: 27
Epoch: 30/500, loss: 34.4906031095141, correct: 27
Epoch: 40/500, loss: 34.486421081189356, correct: 27
Epoch: 50/500, loss: 34.480693085681985, correct: 27
Epoch: 60/500, loss: 34.473178744800634, correct: 27
Epoch: 70/500, loss: 34.46230478962076, correct: 27
Epoch: 80/500, loss: 34.443721159022566, correct: 27
Epoch: 90/500, loss: 34.40625253479988, correct: 27
Epoch: 100/500, loss: 34.34871874110586, correct: 27
Epoch: 110/500, loss: 34.28521154882779, correct: 27
Epoch: 120/500, loss: 34.1987136597797, correct: 27
Epoch: 130/500, loss: 34.07820225106041, correct: 27
Epoch: 140/500, loss: 33.89692183040635, correct: 27
Epoch: 150/500, loss: 33.61323571457739, correct: 28
Epoch: 160/500, loss: 33.15551077055137, correct: 34
Epoch: 170/500, loss: 32.39506992389496, correct: 36
Epoch: 180/500, loss: 31.268882672802384, correct: 38
Epoch: 190/500, loss: 30.001473456512656, correct: 38
Epoch: 200/500, loss: 29.029169502728045, correct: 38
Epoch: 210/500, loss: 28.14709281000799, correct: 39
Epoch: 220/500, loss: 27.385942007433158, correct: 39
Epoch: 230/500, loss: 26.719198537471136, correct: 39
Epoch: 240/500, loss: 26.245635697020177, correct: 39
Epoch: 250/500, loss: 25.8246814086695, correct: 39
Epoch: 260/500, loss: 25.515170417019053, correct: 39
Epoch: 270/500, loss: 25.292336052579266, correct: 39
Epoch: 280/500, loss: 25.121278290242987, correct: 39
Epoch: 290/500, loss: 24.742309087281104, correct: 39
Epoch: 300/500, loss: 24.627497286740645, correct: 39
Epoch: 310/500, loss: 24.223590067285457, correct: 39
Epoch: 320/500, loss: 24.135041949104398, correct: 39
Epoch: 330/500, loss: 24.655017948610737, correct: 39
Epoch: 340/500, loss: 23.797701923077625, correct: 39
Epoch: 350/500, loss: 23.656842615098103, correct: 39
Epoch: 360/500, loss: 23.421854334014814, correct: 40
Epoch: 370/500, loss: 23.60344307065744, correct: 39
Epoch: 380/500, loss: 23.23511685058316, correct: 40
Epoch: 390/500, loss: 23.160357373460084, correct: 40
Epoch: 400/500, loss: 23.88530604016914, correct: 38
Epoch: 410/500, loss: 22.986423721138358, correct: 40
Epoch: 420/500, loss: 22.929279332030625, correct: 40
Epoch: 430/500, loss: 22.84954967360369, correct: 40
Epoch: 440/500, loss: 22.867702505837933, correct: 40
Epoch: 450/500, loss: 22.84475192920354, correct: 39
Epoch: 460/500, loss: 22.79975005745898, correct: 39
Epoch: 470/500, loss: 22.772289247762515, correct: 39
Epoch: 480/500, loss: 22.643541261085893, correct: 40
Epoch: 490/500, loss: 22.920725985666802, correct: 40
Epoch: 500/500, loss: 22.657729676984463, correct: 40

5. Circle
Number of points: 50
Size of Hidden Layer: 2
Learning Rate: 0.5
Number of Epochs: 500.
Epoch 500/500. Time per epoch: 0.034s. Time left: 0.00s.
Logs:
Epoch: 0/500, loss: 0, correct: 0
Epoch: 10/500, loss: 29.602367740029127, correct: 36
Epoch: 20/500, loss: 29.539513627909578, correct: 36
Epoch: 30/500, loss: 29.473549858751294, correct: 36
Epoch: 40/500, loss: 29.40193220952602, correct: 36
Epoch: 50/500, loss: 29.322929977717596, correct: 36
Epoch: 60/500, loss: 29.23592251177801, correct: 36
Epoch: 70/500, loss: 29.142204844447768, correct: 36
Epoch: 80/500, loss: 29.045790935611596, correct: 36
Epoch: 90/500, loss: 28.932047108984975, correct: 36
Epoch: 100/500, loss: 28.378386864315257, correct: 36
Epoch: 110/500, loss: 27.81035858878784, correct: 36
Epoch: 120/500, loss: 27.38489315800892, correct: 36
Epoch: 130/500, loss: 26.952119117762802, correct: 36
Epoch: 140/500, loss: 26.590996887260236, correct: 36
Epoch: 150/500, loss: 26.307364096921177, correct: 36
Epoch: 160/500, loss: 26.033375100537246, correct: 36
Epoch: 170/500, loss: 25.661914139215007, correct: 36
Epoch: 180/500, loss: 25.17141160195151, correct: 36
Epoch: 190/500, loss: 24.872166108173126, correct: 36
Epoch: 200/500, loss: 24.501139710724157, correct: 36
Epoch: 210/500, loss: 24.212791105982387, correct: 36
Epoch: 220/500, loss: 24.01289746104826, correct: 36
Epoch: 230/500, loss: 23.815180255595504, correct: 36
Epoch: 240/500, loss: 23.35257300261648, correct: 36
Epoch: 250/500, loss: 22.92732612515415, correct: 36
Epoch: 260/500, loss: 22.48769318553327, correct: 36
Epoch: 270/500, loss: 22.919124623313373, correct: 36
Epoch: 280/500, loss: 22.735284112218153, correct: 36
Epoch: 290/500, loss: 22.9468964776018, correct: 36
Epoch: 300/500, loss: 21.26007421571551, correct: 33
Epoch: 310/500, loss: 21.77226638483161, correct: 35
Epoch: 320/500, loss: 21.525613200265706, correct: 35
Epoch: 330/500, loss: 20.2558991234009, correct: 36
Epoch: 340/500, loss: 19.015771810120505, correct: 37
Epoch: 350/500, loss: 18.978494005054173, correct: 37
Epoch: 360/500, loss: 17.822689534211104, correct: 39
Epoch: 370/500, loss: 17.983932583457243, correct: 38
Epoch: 380/500, loss: 17.23982087186483, correct: 40
Epoch: 390/500, loss: 18.213931631055022, correct: 38
Epoch: 400/500, loss: 18.71313718673647, correct: 38
Epoch: 410/500, loss: 17.82555057899019, correct: 39
Epoch: 420/500, loss: 17.43325224066316, correct: 40
Epoch: 430/500, loss: 18.640414850236645, correct: 38
Epoch: 440/500, loss: 19.65017837197667, correct: 38
Epoch: 450/500, loss: 16.472129692195466, correct: 40
Epoch: 460/500, loss: 16.000203180550702, correct: 41
Epoch: 470/500, loss: 16.280312435922422, correct: 40
Epoch: 480/500, loss: 17.130815697512574, correct: 40
Epoch: 490/500, loss: 18.07894409661277, correct: 40
Epoch: 500/500, loss: 16.815021447632983, correct: 40



6. Spiral
Number of points: 50
Size of Hidden Layer: 2
Learning Rate: 0.5
Number of Epochs: 500.
Epoch 500/500. Time per epoch: 0.036s. Time left: 0.00s.
Logs:
Epoch: 0/500, loss: 0, correct: 0
Epoch: 10/500, loss: 34.586937111572134, correct: 25
Epoch: 20/500, loss: 34.48583814544609, correct: 29
Epoch: 30/500, loss: 34.42084090883157, correct: 29
Epoch: 40/500, loss: 34.382889909657116, correct: 29
Epoch: 50/500, loss: 34.323791025692344, correct: 29
Epoch: 60/500, loss: 34.26929336133635, correct: 29
Epoch: 70/500, loss: 34.21314238842933, correct: 29
Epoch: 80/500, loss: 34.15761671074815, correct: 29
Epoch: 90/500, loss: 34.10281934980001, correct: 29
Epoch: 100/500, loss: 34.04769944684686, correct: 28
Epoch: 110/500, loss: 33.99108930762705, correct: 28
Epoch: 120/500, loss: 33.930575674641936, correct: 28
Epoch: 130/500, loss: 33.870134683920604, correct: 29
Epoch: 140/500, loss: 33.81460315375166, correct: 28
Epoch: 150/500, loss: 33.76081559853232, correct: 29
Epoch: 160/500, loss: 33.71026545853583, correct: 29
Epoch: 170/500, loss: 33.66374408227864, correct: 29
Epoch: 180/500, loss: 33.62099399330445, correct: 29
Epoch: 190/500, loss: 33.57501987850562, correct: 29
Epoch: 200/500, loss: 33.535591998430995, correct: 29
Epoch: 210/500, loss: 33.49156909142174, correct: 29
Epoch: 220/500, loss: 33.45314402679222, correct: 28
Epoch: 230/500, loss: 33.40879646572463, correct: 28
Epoch: 240/500, loss: 33.36396843498973, correct: 28
Epoch: 250/500, loss: 33.321267170326706, correct: 29
Epoch: 260/500, loss: 33.27792813925641, correct: 28
Epoch: 270/500, loss: 33.234513109122204, correct: 29
Epoch: 280/500, loss: 33.193578803049085, correct: 29
Epoch: 290/500, loss: 33.15275053235498, correct: 29
Epoch: 300/500, loss: 33.11188982427068, correct: 29
Epoch: 310/500, loss: 33.06974328565222, correct: 29
Epoch: 320/500, loss: 33.024599702286565, correct: 29
Epoch: 330/500, loss: 32.98184300657229, correct: 29
Epoch: 340/500, loss: 32.94781310611636, correct: 29
Epoch: 350/500, loss: 32.904680714744806, correct: 29
Epoch: 360/500, loss: 32.85733063976415, correct: 29
Epoch: 370/500, loss: 32.76767073093342, correct: 29
Epoch: 380/500, loss: 32.688083063737125, correct: 29
Epoch: 390/500, loss: 32.58182985073953, correct: 29
Epoch: 400/500, loss: 32.5325417306187, correct: 29
Epoch: 410/500, loss: 32.44652907000422, correct: 29
Epoch: 420/500, loss: 32.36585113748369, correct: 29
Epoch: 430/500, loss: 32.26987109314575, correct: 29
Epoch: 440/500, loss: 32.22179613478583, correct: 29
Epoch: 450/500, loss: 32.20451213118592, correct: 29
Epoch: 460/500, loss: 32.17829472779323, correct: 29
Epoch: 470/500, loss: 32.112608985634495, correct: 29
Epoch: 480/500, loss: 32.06042952356934, correct: 29
Epoch: 490/500, loss: 32.052822143283265, correct: 29
Epoch: 500/500, loss: 32.01868930408452, correct: 27