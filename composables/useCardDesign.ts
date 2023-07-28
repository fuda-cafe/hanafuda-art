const DESIGNS = [
    "cherry-version",
    "koinobori",
    "sabling-art",
] as const;

type CardDesign = typeof DESIGNS[number];

export const useCardDesign = () => {
    const useDesign = (): Ref<CardDesign> => useState("design", () => "cherry-version");
    const useDesignPath = (cardName: string) => `${useDesign().value}/webp/${cardName}.webp`;
    
    const currentDesign = useDesign();

    onMounted(() => {
        watchEffect(() => {
            document?.body.classList.add(currentDesign.value);
        })
    })

    return {
        useDesign,
        useDesignPath
    }
}