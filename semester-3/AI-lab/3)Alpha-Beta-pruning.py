Min,Max=-1000,1000
def minimax (depth,nodeindex,maximizingp,values,alpha,beta):
    if depth==3:
        return values[nodeindex]
    if maximizingp:
        best=Min
        for i in range (0,2):
            val=minimax(depth+1,nodeindex*2+i,False,values,alpha,beta)
            best=max(best,val)
            alpha=max(alpha,best)
            if beta<=alpha:
                break
        return best
    else:
        best=Max
        for i in range (0,2):
            val= minimax(depth+1,nodeindex*2+i,True,values,alpha,beta)
            best=min(best,val)
            beta=min(beta,best)
            if beta<=alpha:
                break
        return best

values=[3,3,4,5,3,5,6,3,5,-1,3,4]           
print("the optimum value is",minimax(0,0,True,values,Min,Max))


