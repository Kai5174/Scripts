import pyperclip
while True:
    q_num = input()
    msg = '''
\\begin{figure}[!ht]
\centering
\includegraphics[width=0.7\\textwidth]{q%s}
\caption{Screen shot for Question %s.%s}
\label{fig:q%s}
\end{figure}
'''% (q_num, q_num[0], q_num[1:], q_num)
    print(msg)
    pyperclip.copy(msg)
