.class final Linfo/sweetduet/ksnctf/jewel/a;
.super Ljava/lang/Object;

# interfaces
.implements Landroid/content/DialogInterface$OnClickListener;


# instance fields
.field private synthetic a:Linfo/sweetduet/ksnctf/jewel/JewelActivity;


# direct methods
.method constructor <init>(Linfo/sweetduet/ksnctf/jewel/JewelActivity;)V
    .locals 0

    iput-object p1, p0, Linfo/sweetduet/ksnctf/jewel/a;->a:Linfo/sweetduet/ksnctf/jewel/JewelActivity;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public final onClick(Landroid/content/DialogInterface;I)V
    .locals 1

    iget-object v0, p0, Linfo/sweetduet/ksnctf/jewel/a;->a:Linfo/sweetduet/ksnctf/jewel/JewelActivity;

    invoke-virtual {v0}, Linfo/sweetduet/ksnctf/jewel/JewelActivity;->finish()V

    return-void
.end method
